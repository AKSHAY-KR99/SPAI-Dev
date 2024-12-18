from datetime import datetime
from io import BytesIO

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import User, Manuscript


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return result.getvalue()
    return None


def get_registration_num():
    # import pdb;pdb.set_trace()
    reg_no = "SPAILM"
    year = datetime.now().year
    reg_no = reg_no + str(year)
    user = User.objects.filter(admin_approved=True, user_role=2).order_by('-date_approved').first()
    if user and user.reg_no is not None:
        reg = user.reg_no
        reg = reg[10:]
        reg = int(reg) + 1
        reg_no = reg_no + str(reg)
    else:
        reg_no = reg_no + "1"
    return reg_no


def get_research_paper_no():
    num = "SPAIRP"
    year = datetime.now().year
    num = num + str(year)
    rp = Manuscript.objects.all().order_by('-date_created').first()
    if rp and rp.paper_no is not None:
        n = rp.paper_no
        n = n[10:]
        n = int(n) + 1
        num = num + str(n)
    else:
        num = num + "1"
    return num


def send_mail_to_executives(user, host):
    executives = User.objects.filter(executive__in=[settings.SECRETARY, settings.PRESIDENT])
    if executives:
        executive_emails = [user.email for user in executives]
        subject = "SPAI New Member Registration"
        link = f"{host}/user/detail/{user.slug_value}"
        message = (
            "New registration noticed.\n"
            f"Name : {user.first_name} {user.last_name}\n"
            f"Email : {user.email}\n"
            f"Approval link : {link}"
            )

        sender_email = "SPAI Online <spai05138@gmail.com>"
        recipient_list = executive_emails

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=sender_email,
            to=recipient_list,
        )
        try:
            email.send()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
