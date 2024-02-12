from django.db import models

# Create your models here.

class IMUser(AbstractUser):
    
    UserType=(
        
         ("EIT", 'EIT'),
         ('TF', "Teaching_Fellow"),
         ("ADS", "Admin_Staff"),
         ("ADM", "Admin"),
        
       
    )
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length =15),
    is_active = models.BooleanField(default=True),
    user_type = models.CharField(choices=UserType.choice),
    
    def __str__(self) -> str:
        return self.username
    
    #Cohort(name, description, year, start_date, end_date, is_active, date_created, date_modified, author [should reference IMUser model])
#CohorMember(cohort[Should reference Cohort model], member [should reference IMUser], is_active, date_created, date_modified, author [should reference IMUser model])
    
    class Cohort(models.Model):
        name = models.CharField(max_length=30),
        description = models.TextField(max_lenth=200),
        year = models.IntegerField(),
        start_date = models.DateField(),
        end_date = models.DateField(),
        is_active = models.BooleanField(default=False ),
        date_created = models.DateTimeField(),
        date_modified = models.DateTimeField(),
        author = models.ForeignKey(IMUser),
        
        def __str__(self) -> str:
            return self.name
        
    class CohorMember(models.Model):
        cohort = models.ForeignKey(Cohort),
        member = models.ForeignKey(IMUser),
        is_active = models.BooleanField(default=True),
        date_created = models.DateTimeField(),
        date_modified = models.DateTimeField(),
        author = models.ForeignKey(IMUser),
        
       
        
  
    
        
        
        
    
        
        
        
        
        
         
              
        