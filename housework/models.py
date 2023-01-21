from django.db import models
from django.utils import timezone

# Create your models here.

HOUSEWORK_CATEGORY = [('cooking','料理'),('washing dish','皿洗い'),('kitchen','キッチン'),('sink drain','シンク排水溝'),
('laundry','洗濯干し'),('fold','洗濯たたみ'),('wash basin','手洗い場'),('bath','お風呂'),('toilet','トイレ'),('trash','ゴミ出し'),('floor','床掃除'),]
USER = [('tekate','テカテ'),('emi','エミ'),]

class HouseworkModel(models.Model):
    postdate = models.DateField(default=timezone.now,verbose_name = '日付')
    category = models.CharField(max_length=50,choices=HOUSEWORK_CATEGORY,verbose_name = '家事')
    username = models.CharField(max_length=50,choices=USER,verbose_name = '担当者')
    suntext = models.TextField(verbose_name = 'メモ')
