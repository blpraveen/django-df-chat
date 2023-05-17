from .models import Message
from .models import MessageImage
from .models import Room
from .models import RoomUser
from .models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()

class RoomUserInline(admin.TabularInline):
    model = RoomUser


@admin.register(RoomUser)
class RoomUserAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "is_active", "is_online")
    list_filter = ("is_active", "is_online", "room__title")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "creator",
        "created",
    )


class MessageImageInline(admin.TabularInline):
    model = MessageImage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    def room(self, obj):
        return obj.room_user.room

    list_display = ("room", "body", "room_user", "parent", "created", "modified")

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    can_delete = False
    verbose_name = "User profile"
    verbose_name_plural = 'Profiles'
    classes = ('text-capitalize','collapse open')
    extra = 1
    max_num = 0
    #fields = [ 'display_avatar','bio','display','avatar']
    list_display = ('avatar_tag')
    fieldsets =  (
        ("Profile", {'fields': ('avatar','bio', 'display',)}),)
    readonly_fields = ['id','avatar_tag']
    # def display_avatar(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
    #         url=obj.avatar.url, # once again, this is the name of the actual image field in your model
    #         width=obj.avatar.width, # or define custom width
    #         height=obj.avatar.height, # same as above
    #         ))
    

class UserProfileAdmin(UserAdmin):
    
    inlines = (UserProfileInline,)

    



admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

#admin.site.register(UserProfile, UserProfileAdmin)