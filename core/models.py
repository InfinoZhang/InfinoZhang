from django.db import models


class Contract(models.Model):
    company = models.CharField('企业名称', max_length=120)
    name = models.CharField('姓名', max_length=80)
    email = models.EmailField('邮箱', blank=True)
    phone = models.CharField('电话', max_length=40, blank=True)
    category = models.CharField('产品品类', max_length=120, blank=True)
    sku = models.CharField('SKU 数量', max_length=80, blank=True)
    timeline = models.DateField('交付时间', null=True, blank=True)
    asset_type = models.CharField('需要内容', max_length=40, blank=True)
    budget = models.CharField('预算范围', max_length=40, blank=True)
    platform = models.CharField('目标平台', max_length=120, blank=True)
    note = models.TextField('产品图与品牌资料说明', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '联系表单'
        verbose_name_plural = '联系表单'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.company} - {self.name}'
