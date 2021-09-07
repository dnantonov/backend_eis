from django.shortcuts import render
from django.views import View

from payments.models import Payment, Accrual


class PaymentView(View):
    template_name = 'payments.html'

    all_accruals = Accrual.objects.all()  # Получаем все задолженности из БД
    all_payments = Payment.objects.all()  # Получаем все платежи из БД
    payments = list(all_payments)
    accruals = list(all_accruals)
    payment_dict = {}  # Создаем словарь в котором будем хранить платежи

    # Проходим по всем платежам и задолженностям в цикле
    for payment in payments:
        for accrual in accruals:
            # Если дата платежа раньше даты задолженности и месяцы совпадают добавляем значение в словарь
            # Данные будут хранится в виде ключ-значение, где платеж-ключ, а значение-задолженность, если она есть
            if payment.date > payment.date and payment.month == payment.month:
                payment_dict[payment] = accrual
            # Если дата платежа раньше даты задолженности, платежа нет в словаре и задолженности нет в значениях
            # добавляем последнюю неоплаченную задолженность. Месяцы не совпадают.
            elif payment.date > accrual.date and payment not in payment_dict.keys() and \
                    accrual not in payment_dict.values():
                payment_dict[payment] = accrual

    # В новом цикле проходим по платежам и смотрим есть ли платежи, которые не были добавлены в словарь.
    # Если такой есть присваиваем ему значение "Платеж без долга" и добавляем в словарь
    for p in payments:
        if p not in payment_dict.keys():
            payment_dict[p] = 'Платеж без долга'

    def get(self, request):
        # Передаем данные в шаблон
        context = {'payments': self.payment_dict}
        return render(request, self.template_name, context)
