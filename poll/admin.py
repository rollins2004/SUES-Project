from django.contrib import admin
from .models import StudentProfile, Candidate, Vote, ElectionPhase

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'Full_name', 'registration_number', 'course', 'year']
    search_fields = ['user__username', 'Full_name', 'registration_number']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'votes']
    search_fields = ['name', 'position']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'candidate', 'position', 'voted_at']
    search_fields = ['voter__username', 'candidate__name']

@admin.register(ElectionPhase)
class ElectionPhaseAdmin(admin.ModelAdmin):
    list_display = ['phase', 'is_active']