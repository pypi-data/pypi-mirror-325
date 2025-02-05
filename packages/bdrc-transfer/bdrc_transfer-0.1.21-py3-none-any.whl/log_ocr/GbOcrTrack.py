#!/usr/bin/env python3
"""
repository for GB OCR status.
Uses the DrsDbContext and the drs models.
Focus on GB processing tracking

You can run this file directly from the command line, which will update
the database with the contents of a "content" log file (see ao-google-books/README.md)
"""
import argparse
import csv
import logging
from datetime import datetime
from pathlib import Path
from ast import literal_eval as make_tuple

import sqlalchemy.exc
# Just use everything
from BdrcDbLib.DbOrm.models.drs import *

# Claims to work, https://pydoc.dev/sqlalchemy/latest/sqlalchemy.dialects.mysql.dml.Insert.html
# but doesn't
from sqlalchemy.dialects.mysql.dml import insert

from BdrcDbLib.DbOrm.DrsContextBase import DrsDbContextBase


class GbOcrContext(DrsDbContextBase):
    """
    Context which just holds some adds/updates for specific tables
    """

    def add_metadata_upload(self, work_name: str, metadata_upload_date: datetime, upload_result: int):
        """
        Adds a metadata upload record
        :type work_name: str
        :param work_name: the BDRC work name
        :type metadata_upload_date: datetime
        :param metadata_upload_date:
        :param upload_result: return code from upload
        """

        w = self.get_or_create_work(work_name)
        self.session.add(
            GbMetadata(work_id=w.workId, upload_time=metadata_upload_date,
                       upload_result=upload_result))
        self.session.flush()
        self.session.commit()

    def add_content_activity(self, work_rid: str, image_group_label: str, activity: str,
                             start_time: datetime, activity_rc: int, log_data: str = ''):
        """
        :param work_rid: Work containing image group
        :param image_group_label: entity to track
        :param activity: activity type (freeform)
        :param start_time: time of activity start
        :param activity_rc: if 0 , success
        :param log_data: user defined data
        :return:
        """
        try:
            v: Volumes = self.get_or_create_volume(work_name=work_rid, volume_name=image_group_label)
            self.session.add(
                GbContent(volume_id=v.volumeId, step_time=start_time, job_step=activity, step_rc=activity_rc,
                          gb_log=log_data))
            self.session.flush()
            self.session.commit()
        except sqlalchemy.exc.DatabaseError as e:
            logging.exception(e)
            self.session.rollback()

    def add_content_state(self, work_rid: str, image_group_label: str, key_date: datetime, state: str, log: str):
        """
        Reflects changes in state of works on GRIN pages. Does NOT reflect activity, such as downloads
        :param work_rid: Work Name
        :param image_group_label: Image group label
        :param key_date: Date of activity
        :param state: which page is sending this
        :param log: json string of other page data (no format)
        :return:
        """
        logging.debug(
            f"args: work_rid :{work_rid}:  image_group_label:{image_group_label}  key_date :{key_date} state:{state}: "
            f"log:{log}")

        # Nice, but not needed
        # stmt = select(GbState).where(and_(GbState.volume_id == v.volumeId, GbState.job_state == state))
        # has_any = self.drs_session.execute(stmt)
        # for gb_track in has_any.scalars():
        #     print(f"{gb_track.volume_id}  {gb_track.job_state}")
        try:
            v: Volumes = self.get_or_create_volume(work_name=work_rid, volume_name=image_group_label)
            # is it a time thing?
            # exec_date: str = key_date.strftime("%")
            # Sigh - on duplicate key update doesnt work for composite keys in SQLAlchemy. This doesn't work either:
            # File "/Users/jimk/dev/ao-google-books/venv/lib/python3.9/site-packages/sqlalchemy/engine/base.py",
            # line 1548, in _execute_clause element keys = sorted(distilled_params[0]) TypeError: '<' not supported
            # between instances of 'str' and 'int' regardless if ON DUPLICATE KEY UPDATE or not
            # self.drs_session.execute( # ON DUPLICATE KEY UPDATE (gb_log) Values (?)...., log f"INSERT INTO {
            # GbState.__table__} (volume_id, job_state, state_date, gb_log) VALUES (?, ?, ?, ?) ;", (_v, state,
            # key_date.strftime("%y/%m/%dT%H:%M:%S"), log) ) self.drs_session.execute( # ...., log f"INSERT INTO {
            # GbState.__table__} (volume_id, job_state, state_date, gb_log) VALUES (?, ?, ?, ?) ON DUPLICATE KEY
            # UPDATE (gb_log) Values (?);", (_v, state, key_date.strftime("%y/%m/%dT%H:%M:%S"), log,
            # log) ) self.drs_session.commit()
            ins = insert(GbState).values(volume_id=v.volumeId, job_state=state, gb_log=log, state_date=key_date)
            ins.on_duplicate_key_update(gb_log=ins.inserted.gb_log)
            self.session.execute(ins)
            self.session.commit()
        except sqlalchemy.exc.DatabaseError as e:
            logging.exception(e)
            self.session.rollback()

    def add_download(self, work_name: str, volume_label: str, download_path: Path, download_object: str):
        """
        Adds a download record
        :param work_name:
        :param volume_label:
        :param download_path:
        :param download_object:
        :return:
        """
        try:
            vol: Volumes = self.get_or_create_volume(work_name, volume_label)
            down_record = GbDownload(
                volume=vol,
                download_time=datetime.now(),
                download_path=str(download_path),
                download_object_name=download_object)
            self.session.add(down_record)
            self.session.commit()
        except sqlalchemy.exc.DatabaseError as e:
            logging.exception(e)
            self.session.rollback()


def import_content_activity_from_log(log_file: object, activity: str):
    """
    Creates **content** records from an activity file (not the "runtime" log file)
    TODO: Create metadata records from same.
    :param log_file: Path to input log file
    :param activity: descriptor
    :return:
    Acceptable sample row:
    [ EDT: 2023-07-13 17:08:21 ]:content_upload:success:('W19792', 'W19792-5878', '/mnt/Archive1/92/W1../images/W.5878')
   """

    ac_reader: csv.reader = csv.reader(log_file, delimiter=':')
    # while True:
    with GbOcrContext() as gb_t:
        for row in ac_reader:
            logging.debug(row)

            # Need to unpack the log format a little. When reading
            #  [ EDT: 2023-07-13 19:25:34 ]: ....
            # with ':' as the csv delimiter, it chops the time up
            _d1 = row[1].strip().split(' ')
            log_date = _d1[0]
            log_hours = _d1[1]
            log_min = row[2]
            log_sec = row[3].split(' ')[0]
            # activity: str = 'upload' if 'upload' in row[4] else 'UNKNOWN'
            rc: int = 0 if 'success' in row[5] else 1
            start_time: datetime = datetime.strptime(f"{log_date} {log_hours}-{log_min}-{log_sec}", '%Y-%m-%d %H-%M-%S')

            # only make data if we have success. Fix ao-google-books #69 before enabling failure.
            # NB that failure should have an extra field after the data that should say something about the
            # failure cause.
            if rc == 0:
                log_row_data = make_tuple(row[6])
                gb_t.add_content_activity(work_rid=log_row_data[0], image_group_label=log_row_data[1],
                                          activity=activity,
                                          start_time=start_time, activity_rc=rc,
                                          log_data=f"Reconstructed from log jimk (see create_time) {log_row_data[2]}")


if __name__ == '__main__':
    """
    This is a stub test
    To run, Use with a log file 
    """

    try:
        log_date_fmt = '[%Z: %Y-%m-%d %X]'
        logging.basicConfig(format='%(asctime)s:%(name)s-%(levelname)s: %(message)s', level=logging.DEBUG,
                            datefmt=log_date_fmt)
        ap = argparse.ArgumentParser()
        ap.add_argument("log_file", help="tracking log to read", type=argparse.FileType('r'))

        # args = ap.parse_args(['/Users/jimk/prod/aogb68/2023-07-13-content-upload.log'])
        args = ap.parse_args()
        import_content_activity_from_log(args.log_file, 'content')
    except:
        print(__doc__)
