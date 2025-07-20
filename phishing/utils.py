import re
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from apps.settingsmanager.models import Settings

User = get_user_model()

def replace_variables(template_content, user):
    # Fetch the company settings
    # settings = Settings.objects.first()

    # Define the replacements
    replacements = {
        '{fullname}': f"{user.firstname} {user.name}",
        '{lastname}': user.name,
        '{surname}': user.firstname,
        # '{companyname}': settings.company_name if settings else "Company",
        '{companyname}': "Company",
        '{date}': timezone.now().strftime('%Y-%m-%d'),
    }

    # Replace date variables with +/- n days
    date_matches = re.findall(r'{date([+-]\d+)}', template_content)
    for match in date_matches:
        delta_days = int(match)
        new_date = (timezone.now() + timedelta(days=delta_days)).strftime('%Y-%m-%d')
        replacements[f'{match}'] = new_date

    # Replace random variables
    all_users = User.objects.all()
    if all_users.exists():
        random_user = all_users.order_by('?').first()
        replacements.update({
            '{random.lastname}': random_user.name,
            '{random.fullname}': f"{random_user.firstname} {random_user.name}",
            '{random.surname}': random_user.firstname,
        })

    # Replace job function-specific random variables
    job_functions = ['hr', 'finance', 'marketing', 'it']
    for job_function in job_functions:
        job_function_users = User.objects.filter(job_function__name=job_function)
        print("user job functions ", job_function_users)
        if job_function_users.exists():
            random_job_function_user = job_function_users.order_by('?').first()
            replacements.update({
                f'{{random.department.{job_function}.lastname}}': random_job_function_user.name,
                f'{{random.department.{job_function}.fullname}}': f"{random_job_function_user.firstname} {random_job_function_user.name}",
                f'{{random.department.{job_function}.surname}}': random_job_function_user.firstname,
            })

    # Replace the variables in the content
    for key, value in replacements.items():
        print(key, value, "<<<")
        if key and value:
            template_content = template_content.replace(key, value)

    return template_content
