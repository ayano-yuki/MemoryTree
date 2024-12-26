from django.db import models

class DiaryEntry(models.Model):
    title = models.CharField(max_length=200)  # 日記のタイトル
    content = models.TextField()  # 日記の本文
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.title
