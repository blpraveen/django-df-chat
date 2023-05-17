from .models import Message
from .models import MessageImage
from .models import Room
from .models import RoomUser
from .models import UserProfile
from .forms import ProfileUserCreationForm
from .forms import ProfileUserChangeForm
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
    extra = 1 
    classes = ('text-capitalize','collapse open')
    list_display = ("avatar_tag",)
    fieldsets =  (
        (None, {'fields': ('avatar','bio', 'display','avatar_tag')}),)
    readonly_fields = ('avatar_tag',)



class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    
    


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

#admin.site.register(UserProfile, UserProfileAdmin)