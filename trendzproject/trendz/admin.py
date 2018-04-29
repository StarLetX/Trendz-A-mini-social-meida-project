from django.contrib import admin
from trendz.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info', 'Area','Number','Facebook','WhatsApp')


	def user_info(self, obj):
		return obj


	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('Number')
		return queryset


	user_info.short_description = "Info"


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.site_header = "ADMIN PANEL"

