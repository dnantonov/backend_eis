from django.db.models import Count, Max
from django.http import JsonResponse
from django.views import View

from actions.models import Action


class ActionView(View):
    queryset = Action.objects.values('session__account__number', 'action_type')\
        .annotate(last=Max('created_at'), count=Count('action_type')).order_by('session')

    actions = {}
    actions_list = []
    for q in queryset:
        # Проходимся по queryset и создаем для каждого пользователя дефолтные значения
        if q['session__account__number'] not in actions.keys():
            actions[q['session__account__number']] = [
                {'action_type': 'Create', 'last': 'Null', 'count': 0},
                {'action_type': 'Read', 'last': 'Null', 'count': 0},
                {'action_type': 'Update', 'last': 'Null', 'count': 0},
                {'action_type': 'Delete', 'last': 'Null', 'count': 0},
            ]
        # Достаем из queryset значения по каждому действию
        data = {
            'action_type': q['action_type'],
            'last': q['last'],
            'count': q['count']
        }
        # Записываем данные для каждого пользователя по каждому действию если оно имеется
        for item in actions[q['session__account__number']]:
            if item['action_type'] == data['action_type']:
                ind = actions[q['session__account__number']].index(item)
                actions[q['session__account__number']][ind] = data

    def get(self, request):
        # Отдаем данные в формате json
        data = self.actions
        return JsonResponse(data, safe=False)

