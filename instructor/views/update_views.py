from instructor import models as instructor_models
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
import json


@require_POST
@login_required
def update_instructor_category(request):
    try:
        data = json.loads(request.body)
        categories = data.get('categories')
        instructor = instructor_models.Instructor.objects.get(user=request.user)
        instructor.categories.clear()
        instructor.categories.add(*categories)
        instructor.save()

        success_html = render_to_string('components/alert.html', {
            'variant': 'success',
            'message': 'Categories updated successfully.',
            'text_center': 1
        })

        return JsonResponse({'success': True, 'message': 'Categories updated successfully.', 'html': success_html})
    except Exception as e:
        error_html = render_to_string('components/alert.html', {
            'variant': 'danger',
            'message': str(e),
            'text_center': 1
        })
        return JsonResponse({'success': False, 'message': str(e), 'html': error_html})

