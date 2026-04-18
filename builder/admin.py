from django.contrib import admin
from .models import Resume, PersonalDetail, Education, Experience, Skill, Project, Certification

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

class PersonalDetailInline(admin.StackedInline):
    model = PersonalDetail

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'template', 'created_at')
    inlines = [PersonalDetailInline, EducationInline, ExperienceInline, SkillInline, ProjectInline, CertificationInline]

admin.site.register(PersonalDetail)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
