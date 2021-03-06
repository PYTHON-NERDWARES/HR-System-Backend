from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


ROLE = (
    ('HR','HR'),
    ('Branch Manager','Branch Manager'),
    ('Department Manager','Department Manager'),
    ('Software Engineer', 'Software Engineer'),
    ('Senior Software Engineer', 'Senior Software Engineer'),
    ('Full Stack Developer', 'Senior Software Engineer'),
    ('FrontEnd Developer', 'FrontEnd Developer'),
    ('BackEnd Developer', 'BackEnd Developer'),
    ('Python Developer', 'Python Developer'),
    ('UX Designer', 'UX Designer'),
    ('UI Designer', 'UI Designer'),
    ('DOTnet Developer', 'DOTnet Developer'),
    ('Java Developer', 'Java Developer'),
    ('Android Developer', 'Android Developer'),
    ('Mobile Developer', 'Mobile Developer'),
    ('Project Development Manager', 'Project Development Manager'),
    ('Chief Operating Officer', 'Chief Operating Officer'),
    ('Digital Marketing', 'Digital Marketing'),
    ('Marketing Officer', 'Marketing Officer'),
    ('Databace Administrator', 'Databace Administrator'),
    ('Quality Assurance', 'Quality Assurance'),
    ('Junior Frontend Developer', 'Junior Frontend Developer'),
    ('Trainee', 'Trainee'),
)

NATIONALITY = (
    ('Afghan', 'Afghan'),
    ('Albanian', 'Albanian'),
    ('Algerian', 'Algerian'),
    ('Argentinian', 'Argentinian'),
    ('Australian', 'Australian'),
    ('Bangladeshi', 'Bangladeshi'),
    ('Belgian', 'Belgian'),
    ('Bolivian', 'Bolivian'),
    ('Batswana', 'Batswana'),
    ('Brazilian', 'Brazilian'),
    ('Bulgarian', 'Bulgarian'),
    ('Cambodian', 'Cambodian'),
    ('Cameroonian', 'Cameroonian'),
    ('Canadian', 'Canadian'),
    ('Chilean', 'Chilean'),
    ('Chinese', 'Chinese'),
    ('Colombian', 'Colombian'),
    ('Costa Rican', 'Costa Rican'),
    ('Croatian', 'Croatian'),
    ('Cuban', 'Cuban',),
    ('Czech', 'Czech'),
    ('Danish', 'Danish'),
    ('Dominican', 'Dominican'),
    ('Ecuadorian', 'Ecuadorian'),
    ('Egyptian', 'Egyptian'),
    ('Salvadorian', 'Salvadorian'),
    ('English', 'English'),
    ('Estonian', 'Estonian'),
    ('Ethiopian', 'Ethiopian'),
    ('Fijian', 'Fijian'),
    ('Finnish', 'Finnish'),
    ('French', 'French'),
    ('German', 'German'),
    ('Ghanaian', 'Ghanaian'),
    ('Greek', 'Greek',),
    ('Guatemalan', 'Guatemalan'),
    ('Haitian', 'Haitian'),
    ('Honduran', 'Honduran'),
    ('Hungarian', 'Hungarian'),
    ('Icelandic', 'Icelandic'),
    ('Indian', 'Indian'),
    ('Indonesian', 'Indonesian'),
    ('Iranian', 'Iranian'),
    ('Iraqi', 'Iraqi',),
    ('Irish', 'Irish',),
    ('Italian', 'Italian'),
    ('Jamaican', 'Jamaican'),
    ('Japanese', 'Japanese'),
    ('Jordanian', 'Jordanian'),
    ('Kenyan', 'Kenyan'),
    ('Kuwaiti', 'Kuwaiti'),
    ('Lao', 'Lao',), ('Latvian', 'Latvian'),
    ('Lebanese', 'Lebanese'),
    ('Libyan', 'Libyan'),
    ('Lithuanian', 'Lithuanian'),
    ('Malagasy', 'Malagasy'),
    ('Malaysian', 'Malaysian'),
    ('Malian', 'Malian'),
    ('Maltese', 'Maltese'),
    ('Mexican', 'Mexican'),
    ('Mongolian', 'Mongolian'),
    ('Moroccan', 'Moroccan'),
    ('Mozambican', 'Mozambican'),
    ('Namibian', 'Namibian'),
    ('Nepalese', 'Nepalese'),
    ('Dutch', 'Dutch',),
    ('New Zealand', 'New Zealand'),
    ('Nicaraguan', 'Nicaraguan'),
    ('Nigerian', 'Nigerian'),
    ('Norwegian', 'Norwegian'),
    ('Pakistani', 'Pakistani'),
    ('Panamanian', 'Panamanian'),
    ('Paraguayan', 'Paraguayan'),
    ('Peruvian', 'Peruvian'),
    ('Philippine', 'Philippine'),
    ('Polish', 'Polish'),
    ('Portuguese', 'Portuguese'),
    ('Romanian', 'Romanian'),
    ('Russian', 'Russian'),
    ('Saudi', 'Saudi',),
    ('Scottish', 'Scottish'),
    ('Senegalese', 'Senegalese'),
    ('Serbian', 'Serbian'),
    ('Singaporean', 'Singaporean'),
    ('Slovak', 'Slovak'),
    ('South African', 'South African'),
    ('Korean', 'Korean'),
    ('Spanish', 'Spanish'),
    ('Sri Lankan', 'Sri Lankan'),
    ('Sudanese', 'Sudanese'),
    ('Swedish', 'Swedish'),
    ('Swiss', 'Swiss',),
    ('Syrian', 'Syrian'),
    ('Taiwanese', 'Taiwanese'),
    ('Tajikistani', 'Tajikistani'),
    ('Thai', 'Thai',),
    ('Tongan', 'Tongan'),
    ('Tunisian', 'Tunisian'),
    ('Turkish', 'Turkish'),
    ('Ukrainian', 'Ukrainian'),
    ('Emirati', 'Emirati'),
    ('British', 'British'),
    ('American', 'American'),
    ('Uruguayan', 'Uruguayan'),
    ('Venezuelan', 'Venezuelan'),
    ('Vietnamese', 'Vietnamese'),
    ('Welsh', 'Welsh',),
    ('Zambian', 'Zambian'),
    ('Zimbabwean', 'Zimbabwean'),
)

DEPARTMENT = (
    ('Managment', 'Managment'),
    ('Development', 'Development'),
    ('Testing', 'Testing'),
    ('Quality', 'Quality'),
)

WORKTYPE = (
    ('On Site', 'On Site'),
    ('Remote', 'Remote'),
)

MARTIAL = (
    ('Single', 'Single'),
    ('Married', 'Married'),
)

GENDER = (('Male','Male'), ('Female', 'Female'))

from django.utils.timezone import localtime, now
id_date = localtime(now()).date()



def to_integer(id_date):
    return 10000*id_date.year + 100*id_date.month + id_date.day


date = to_integer(id_date)

class CustomUser(AbstractUser):
    password = models.CharField(('password'), max_length=128)
    employee_id = models.CharField(max_length=255 ,default=date, null=True , blank=True)
    role = models.CharField(max_length=50 , choices=ROLE, default='HR', null=True , blank=True)
    work_type = models.CharField(max_length=50, choices=WORKTYPE, null=True , blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True , blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True , blank=True)
    experience = models.IntegerField(default=1 , null=True , blank=True)
    salary =models.FloatField(default="50000",null=True , blank=True)
    gender = models.CharField(choices=GENDER, max_length=10 , null=True , blank=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY, null=True , blank=True)
    marital_status = models.CharField(max_length=50, choices=MARTIAL, null=True , blank=True)
    phone = models.CharField(max_length=15, null=True , blank=True)
    Personal_Picture = models.URLField(max_length=1000, null=True , blank=True)
    annual_off_days = models.IntegerField(default=12, null=True , blank=True)
    days_taken = models.IntegerField(default=0 , null=True , blank=True)
    days_remaining = models.IntegerField(default=0 , null=True , blank=True)
    monthly_permission_hours = models.IntegerField(default=8)
    hours_taken = models.IntegerField(default=0)
    hours_remaining = models.IntegerField(default=8)


####################################################################################################

# print(CustomUser.brnchManagers())


class Branch(models.Model):

    name = models.CharField(max_length=50, null=True , blank=True)
    phone = models.CharField(max_length=15, null=True , blank=True)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    city = models.CharField(max_length=255 ,null=True , blank=True)
    country = models.CharField(max_length=255 ,null=True , blank=True)
    turnover = models.IntegerField(default=5)
    branch_manager = models.CharField(max_length=255 ,null=True , blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    department_manager = models.CharField(max_length=50 ,default='')
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True , blank=True)


    def __str__(self):
        return self.name


class Leave(models.Model):
    name = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True , blank=True)
    branch_name = models.CharField(max_length=255, null=True , blank=True)
    date = models.DateTimeField(default=timezone.now)
    request_status = models.CharField(max_length=50, default='Pending')
    hours = models.IntegerField(default=0 )

    def __str__(self):
        return self.name.first_name +' '+ self.name.last_name
