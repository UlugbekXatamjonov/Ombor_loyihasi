from django.contrib import admin
from .models import Product, Report
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# ----------------------- Product Admin -----------------------
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = False
        fields = ('tur','nom','rang','narx','son','kompania','mudat','kg','izoh','sana')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('tur','nom','rang','narx','avatar','son','sana')
    list_filter = ('tur','nom','rang','sana','kompania')
    search_fields = ('nom',)
    readonly_fields = ('avatar',)
    resource_class = ProductResource


# ---------------------- Report Admin -----------------------
class ReportResource(resources.ModelResource):
    class Meta:
        model = Report
        skip_unchanged = True
        report_skipped = False
        fields = ('tur','nom','rang','son','kompania','mudat','kg','izoh','sana','tekshir')

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
    list_display = ('tur','nom','rang','avatar','son','sana','tekshir')
    list_filter = ('tur','nom','rang','sana','kompania','tekshir')
    search_fields = ('nom',)
    readonly_fields = ('avatar',)
    resource_class = ReportResource
