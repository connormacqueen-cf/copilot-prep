from django.contrib import admin
from .models import CustomUser, Team, Activity, Leaderboard, Workout

admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Leaderboard)
admin.site.register(Workout)
