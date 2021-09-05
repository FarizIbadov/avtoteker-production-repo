from django.contrib import admin
from django.contrib import messages


class CustomAdminActionsMixin(object):  
    def backup(self,modeladmin, request, queryset):
        queryset.backup()
        count = queryset.count() 
        extra = 'item was' if count == 1 else "items were"
        msg = "%d %s restored successfully" % (count,extra)
        messages.add_message(request,messages.SUCCESS,msg,True)
    backup.short_description = "Backup deleted items"

    def force_delete(self,modeladmin, request, queryset):
        queryset.force_delete()
    backup.short_description = "Force delete items"

 
class CustomModelAdmin(admin.ModelAdmin,CustomAdminActionsMixin):
    def get_list_display(self,request):
        list_display = super().get_list_display(request)

        if list_display:
            return (*list_display,"deleted")        
        return ("__str__",'deleted')

    def get_exclude(self,request,obj=None):
        exclude = super().get_exclude(request,obj)
        if exclude:
            return ('deleted',*exclude)
        return ("deleted",)

    def get_list_filter(self,request):
        list_filter = super().get_list_filter(request)
        return ('deleted',*list_filter)

    def get_actions(self,request):
        actions = super().get_actions(request)
        default_actions = self.prepear_actions()
        
        new_actions = {
            **actions,
            **default_actions
        }
        
        return new_actions

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        view = super().changeform_view(request, object_id, form_url, extra_context)
        if request.method == "POST" and object_id and '_backup' in request.POST:
            instance = self.get_object(request, object_id)
            instance.backup()
        return view

    def get_object(self, request, object_id, from_field=None):
        return self.model.objects.get_object(pk=object_id)

    def prepear_actions(self):
        default_action_list = [self.backup,self.force_delete,*self.actions]
        default_actions = {}

        for func in default_action_list:
            name = func.__name__
            action = self.get_action(func)
            default_actions[name] = action

        return default_actions

