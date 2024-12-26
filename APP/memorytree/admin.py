from django.contrib import admin
from .models import DiaryEntry

@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')  # 必要に応じてカスタマイズ
    search_fields = ('title', 'content')
    list_filter = ('created_at',)