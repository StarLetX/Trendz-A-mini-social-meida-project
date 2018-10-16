from django.contrib import admin
from .models import UserProfile
'''

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'user_info', 'area','number')


	def user_info(self, obj):
		return obj


	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('number')
		return queryset


	user_info.short_description = "Info"

admin.site.register(UserProfile, UserProfileAdmin)'''

admin.site.register(UserProfile)
admin.site.site_header = "ADMIN PANEL"

