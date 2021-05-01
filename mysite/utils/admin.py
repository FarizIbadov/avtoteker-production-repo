from django.contrib import admin
 
def backup(modeladmin, request, queryset):
    queryset.update(deleted=False)
backup.short_description = "Backup deleted items"


class CustomModelAdmin(admin.ModelAdmin):
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

    def prepear_actions(self):
        default_action_list = [backup,*self.actions]
        default_actions = {}

        for func in default_action_list:
            name = func.__name__
            action = self.get_action(func)
            default_actions[name] = action

        return default_actions