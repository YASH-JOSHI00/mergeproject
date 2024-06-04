import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Post, User, Category, Tags, Comment, Reply


def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected to CSV"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    Search_Fields=Post.SearchableFields
    list_filter=Post.FilterFields
    actions = [export_as_csv]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields=User.SearchableFields
    actions = [export_as_csv]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'body',)
    search_fields=Comment.SearchableFields
    list_filter=Comment.FilterFields
    actions = [export_as_csv]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=Category.SearchableFields
    list_filter=Category.FilterFields
    actions = [export_as_csv]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=Tags.SearchableFields
    list_filter=Tags.FilterFields
    actions = [export_as_csv]

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('body', 'comment','time', 'post')
    search_fields=Reply.SearchableFields
    list_filter=Reply.FilterFields
    actions = [export_as_csv]