import os
import oss2
from oss2 import SizedFileAdapter, determine_part_size
from oss2.models import PartInfo
from long_utils.storage.aliyun.oss_base import OssBase
from long_utils.storage.config import SSconfig


class AliyumOss(OssBase):
    """
    阿里云OSS对象存储
    文档：
        https://help.aliyun.com/document_detail/32026.html?spm=a2c4g.11186623.6.994.4aff196bVJxXwO
    """

    def __init__(self, config: SSconfig):
        super(AliyumOss, self).__init__(config=config)
        endpoint_host, endpoint_sec = config.bucket_url.split('//')
        object_image_url = f"{endpoint_host}//{config.bucket_name}.{endpoint_sec}"
        self.object_image_url = object_image_url

    def multipart_upload_file(self, key, file, limit_file_size=1024 * 1024 * 20, progress_callback=None):
        """

        :param key: 对象key
        :param file: 要上传的本地文件
        :param limit_file_size: 分片大小
        :param progress_callback: 回调函数
        :return:
        """
        total_size = os.path.getsize(file)
        upload_id = self.bucket.init_multipart_upload(key).upload_id
        part_size = determine_part_size(total_size, preferred_size=limit_file_size)
        parts = []
        is_completed = True
        # 逐个上传分片。
        with open(file, 'rb') as fileobj:
            part_number = 1
            offset = 0
            while offset < total_size:
                num_to_upload = min(part_size, total_size - offset)
                # 调用SizedFileAdapter(fileobj, size)方法会生成一个新的文件对象，重新计算起始追加位置。
                result = self.bucket.upload_part(
                    key=key,
                    upload_id=upload_id,
                    part_number=part_number,
                    data=SizedFileAdapter(fileobj, num_to_upload)
                )
                parts.append(PartInfo(part_number, result.etag))
                offset += num_to_upload
                part_number += 1
                if progress_callback:
                    progress_callback(offset, total_size)
        if is_completed:
            # 完成分片上传
            self.bucket.complete_multipart_upload(key, upload_id, parts)
        else:
            self.bucket.abort_multipart_upload(key, upload_id)

    def object_exists(self, key) -> bool:
        """
        判断一个文件是否存在于oss
        @param key: 文件 key
        @return: bool
        """
        # 返回值为true表示文件存在，false表示文件不存在。
        return self.bucket.object_exists(key)

    def resumable_download(self, key, local_file, progress_callback=None):
        oss2.resumable_download(
            self.bucket,
            key=key,
            filename=local_file,
            progress_callback=progress_callback
        )
