# from django.db import models

# # Create your models here.
# POSITION_CHOICES = [
#         ('ST', 'Striker'),
#         ('RW', 'Right Wing'),
#         ('LW', 'Left Wing'),
#         ('CF', 'Center Forward')
#         ('RF', 'Rigth Forward')
#         ('LF', 'Left Forward')
#         ('CDM', 'Center Defensive Mildfielder')
#         ('LM', 'Left Midfielders')
#         ('RM', 'Right Midfielders')
#         ('CM', 'Center Midfielders')
#         ('CAM', 'Center Attacking Midfielder')
#         ('CB', 'Center Back')
#         ('RB', 'Right Back')
#         ('LB', 'Left Back')
#         ('RWB', 'Right Wing Back')
#         ('LWB', 'Left Wing Back')
#         ('GK', 'Goal Keeper')
#     ]
# NATIONS_CHOICES = [
#       ("Afghanistan", "🇦🇫"),
#     ("Åland Islands", "🇦🇽"),
#     ("Albania", "🇦🇱"),
#     ("Algeria", "🇩🇿"),
#     ("American Samoa", "🇦🇸"),
#     ("Andorra", "🇦🇩"),
#     ("Angola", "🇦🇴"),
#     ("Anguilla", "🇦🇮"),
#     ("Antigua and Barbuda", "🇦🇬"),
#     ("Argentina", "🇦🇷"),
#     ("Armenia", "🇦🇲"),
#     ("Aruba", "🇦🇼"),
#     ("Australia", "🇦🇺"),
#     ("Austria", "🇦🇹"),
#     ("Azerbaijan", "🇦🇿"),
#     ("Bahamas", "🇧🇸"),
#     ("Bahrain", "🇧🇭"),
#     ("Bangladesh", "🇧🇩"),
#     ("Barbados", "🇧🇧"),
#     ("Belarus", "🇧🇾"),
#     ("Belgium", "🇧🇪"),
#     ("Belize", "🇧🇿"),
#     ("Benin", "🇧🇯"),
#     ("Bermuda", "🇧🇲"),
#     ("Bhutan", "🇧🇹"),
#     ("Bolivia", "🇧🇴"),
#     ("Bosnia and Herzegovina", "🇧🇦"),
#     ("Botswana", "🇧🇼"),
#     ("Brazil", "🇧🇷"),
#     ("Virgin Islands, British", "🇻🇬"),
#     ("Brunei Darussalam", "🇧🇳"),
#     ("Bulgaria", "🇧🇬"),
#     ("Burkina Faso", "🇧🇫"),
#     ("Burundi", "🇧🇮"),
#     ("Cabo Verde", "🇨🇻"),
#     ("Cambodia", "🇰🇭"),
#     ("Cameroon", "🇨🇲"),
#     ("Canada", "🇨🇦"),
#     ("Cayman Islands", "🇰🇾"),
#     ("Central African Republic", "🇨🇫"),
#     ("Chad", "🇹🇩"),
#     ("Chile", "🇨🇱"),
#     ("China", "🇨🇳"),
#     ("Colombia", "🇨🇴"),
#     ("Comoros", "🇰🇲"),
#     ("Congo", "🇨🇬"),
#     ("Cook Islands", "🇨🇰"),
#     ("Costa Rica", "🇨🇷"),
#     ("Côte d'Ivoire", "🇨🇮"),
#     ("Croatia", "🇭🇷"),
#     ("Cuba", "🇨🇺"),
#     ("Curaçao", "🇨🇼"),
#     ("Cyprus", "🇨🇾"),
#     ("Czech Republic", "🇨🇿"),
#     ("Congo, Democratic Republic of the", "🇨🇩"),
#     ("Denmark", "🇩🇰"),
#     ("Djibouti", "🇩🇯"),
#     ("Dominica", "🇩🇲"),
#     ("Dominican Republic", "🇩🇴"),
#     ("Ecuador", "🇪🇨"),
#     ("Egypt", "🇪🇬"),
#     ("El Salvador", "🇸🇻"),
#     ("Equatorial Guinea", "🇬🇶"),
#     ("Eritrea", "🇪🇷"),
#     ("Estonia", "🇪🇪"),
#     ("Eswatini", "🇸🇿"),
#     ("Ethiopia", "🇪🇹"),
#     ("Falkland Islands (Malvinas)", "🇫🇰"),
#     ("Faroe Islands", "🇫🇴"),
#     ("Fiji", "🇫🇯"),
#     ("Finland", "🇫🇮"),
#     ("France", "🇫🇷"),
#     ("French Guiana", "🇬🇫"),
#     ("French Polynesia", "🇵🇫"),
#     ("Gabon", "🇬🇦"),
#     ("Gambia", "🇬🇲"),
#     ("Georgia", "🇬🇪"),
#     ("Germany", "🇩🇪"),
#     ("Ghana", "🇬🇭"),
#     ("Gibraltar", "🇬🇮"),
#     ("Greece", "🇬🇷"),
#     ("Greenland", "🇬🇱"),
#     ("Grenada", "🇬🇩"),
#     ("Guadeloupe", "🇬🇵"),
#     ("Guam", "🇬🇺"),
#     ("Guatemala", "🇬🇹"),
#     ("Guernsey", "🇬🇬"),
#     ("Guinea", "🇬🇳"),
#     ("Guinea-Bissau", "🇬🇼"),
#     ("Guyana", "🇬🇾"),
#     ("Haiti", "🇭🇹"),
#     ("Honduras", "🇭🇳"),
#     ("Hong Kong", "🇭🇰"),
#     ("Hungary", "🇭🇺"),
#     ("Iceland", "🇮🇸"),
#     ("India", "🇮🇳"),
#     ("Indonesia", "🇮🇩"),
#     ("Iran", "🇮🇷"),
#     ("Iraq", "🇮🇶"),
#     ("Ireland", "🇮🇪"),
#     ("Isle of Man", "🇮🇲"),
#     ("Israel", "🇮🇱"),
#     ("Italy", "🇮🇹"),
#     ("Jamaica", "🇯🇲"),
#     ("Japan", "🇯🇵"),
#     ("Jersey", "🇯🇪"),
#     ("Jordan", "🇯🇴"),
#     ("Kazakhstan", "🇰🇿"),
#     ("Kenya", "🇰🇪"),
#     ("Kiribati", "🇰🇮"),
#     ("Kosovo", "🇽🇰"),
#     ("Kuwait", "🇰🇼"),
#     ("Kyrgyzstan", "🇰🇬"),
#     ("Lao People's Democratic Republic", "🇱🇦"),
#     ("Latvia", "🇱🇻"),
#     ("Lebanon", "🇱🇧"),
#     ("Lesotho", "🇱🇸"),
#     ("Liberia", "🇱🇷"),
#     ("Libya", "🇱🇾"),
#     ("Liechtenstein", "🇱🇮"),
#     ("Lithuania", "🇱🇹"),
#     ("Luxembourg", "🇱🇺"),
#     ("Macao", "🇲🇴"),
#     ("Madagascar", "🇲🇬"),
#     ("Malawi", "🇲🇼"),
#     ("Malaysia", "🇲🇾"),
#     ("Maldives", "🇲🇻"),
#     ("Mali", "🇲🇱"),
#     ("Malta", "🇲🇹"),
#     ("Marshall Islands", "🇲🇭"),
#     ("Martinique", "🇲🇶"),
#     ("Mauritania", "🇲🇷"),
#     ("Mauritius", "🇲🇺"),
#     ("Mayotte", "🇾🇹"),
#     ("Mexico", "🇲🇽"),
#     ("Micronesia", "🇫🇲"),
#     ("Moldova", "🇲🇩"),
#     ("Monaco", "🇲🇨"),
#     ("Mongolia", "🇲🇳"),
#     ("Montenegro", "🇲🇪"),
#     ("Montserrat", "🇲🇸"),
#     ("Morocco", "🇲🇦"),
#     ("Mozambique", "🇲🇿"),
#     ("Myanmar", "🇲🇲"),
#     ("Namibia", "🇳🇦"),
#     ("Nauru", "🇳🇷"),
#     ("Nepal", "🇳🇵"),
#     ("Netherlands", "🇳🇱"),
#     ("New Caledonia", "🇳🇨"),
#     ("New Zealand", "🇳🇿"),
#     ("Nicaragua", "🇳🇮"),
#     ("Niger", "🇳🇪"),
#     ("Nigeria", "🇳🇬"),
#     ("Niue", "🇳🇺"),
#     ("North Korea", "🇰🇵"),
#     ("North Macedonia", "🇲🇰"),
#     ("Northern Mariana Islands", "🇲🇵"),
#     ("Norway", "🇳🇴"),
#     ("Oman", "🇴🇲"),
#     ("Pakistan", "🇵🇰"),
#     ("Palau", "🇵🇼"),
#     ("Palestine", "🇵🇸"),
#     ("Panama", "🇵🇦"),
#     ("Papua New Guinea", "🇵🇬"),
#     ("Paraguay", "🇵🇾"),
#     ("Peru", "🇵🇪"),
#     ("Philippines", "🇵🇭"),
#     ("Poland", "🇵🇱"),
#     ("Portugal", "🇵🇹"),
#     ("Puerto Rico", "🇵🇷"),
#     ("Qatar", "🇶🇦"),
#     ("Réunion", "🇷🇪"),
#     ("Romania", "🇷🇴"),
#     ("Russian Federation", "🇷🇺"),
#     ("Rwanda", "🇷🇼"),
#     ("Saint Barthélemy", "🇧🇱"),
#     ("Saint Helena, Ascension and Tristan da Cunha", "🇸🇭"),
#     ("Saint Kitts and Nevis", "🇰🇳"),
#     ("Saint Lucia", "🇱🇨"),
#     ("Saint Pierre and Miquelon", "🇵🇲"),
#     ("Saint Vincent and the Grenadines", "🇻🇨"),
#     ("Samoa", "🇼🇸"),
#     ("San Marino", "🇸🇲"),
#     ("Sao Tome and Principe", "🇸🇹"),
#     ("Saudi Arabia", "🇸🇦"),
#     ("Senegal", "🇸🇳"),
#     ("Serbia", "🇷🇸"),
#     ("Seychelles", "🇸🇨"),
#     ("Sierra Leone", "🇸🇱"),
#     ("Singapore", "🇸🇬"),
#     ("Sint Maarten (Dutch part)", "🇸🇽"),
#     ("Slovakia", "🇸🇰"),
#     ("Slovenia", "🇸🇮"),
#     ("Solomon Islands", "🇸🇧"),
#     ("Somalia", "🇸🇴"),
#     ("South Africa", "🇿🇦"),
#     ("Korea", "🇰🇷"),
#     ("South Sudan", "🇸🇸"),
#     ("Spain", "🇪🇸"),
#     ("Sri Lanka", "🇱🇰"),
#     ("Sudan", "🇸🇩"),
#     ("Suriname", "🇸🇷"),
#     ("Sweden", "🇸🇪"),
#     ("Switzerland", "🇨🇭"),
#     ("Syria", "🇸🇾"),
#     ("Taiwan", "🇹🇼"),
#     ("Tajikistan", "🇹🇯"),
#     ("Tanzania", "🇹🇿"),
#     ("Thailand", "🇹🇭"),
#     ("Timor-Leste", "🇹🇱"),
#     ("Togo", "🇹🇬"),
#     ("Tokelau", "🇹🇰"),
#     ("Tonga", "🇹🇴"),
#     ("Trinidad and Tobago", "🇹🇹"),
#     ("Tunisia", "🇹🇳"),
#     ("Turkey", "🇹🇷"),
#     ("Turkmenistan", "🇹🇲"),
#     ("Turks and Caicos Islands", "🇹🇨"),
#     ("Tuvalu", "🇹🇻"),
#     ("Uganda", "🇺🇬"),
#     ("Ukraine", "🇺🇦"),
#     ("United Arab Emirates", "🇦🇪"),
#     ("United Kingdom", "🇬🇧"),
#     ("United States of America", "🇺🇸"),
#     ("Uruguay", "🇺🇾"),
#     ("Virgin Islands, U.S.", "🇻🇮"),
#     ("Uzbekistan", "🇺🇿"),
#     ("Vanuatu", "🇻🇺"),
#     ("Holy See", "🇻🇦"),
#     ("Venezuela", "🇻🇪"),
#     ("Vietnam", "🇻🇳"),
#     ("Wallis and Futuna", "🇼🇫"),
#     ("Western Sahara", "🇪🇭"),
#     ("Yemen", "🇾🇪"),
#     ("Zambia", "🇿🇲"),
#     ("Zimbabwe", "🇿🇼"),
# ]

# CLUB_CHOICES = {
#     "🇬🇧 Premier League": [
#         ("Arsenal", "🇬🇧"),
#         ("Aston Villa", "🇬🇧"),
#         ("Brentford", "🇬🇧"),
#         ("Brighton & Hove Albion", "🇬🇧"),
#         ("Chelsea", "🇬🇧"),
#         ("Crystal Palace", "🇬🇧"),
#         ("Everton", "🇬🇧"),
#         ("Fulham", "🇬🇧"),
#         ("Liverpool", "🇬🇧"),
#         ("Manchester City", "🇬🇧"),
#         ("Manchester United", "🇬🇧"),
#         ("Newcastle United", "🇬🇧"),
#         ("Nottingham Forest", "🇬🇧"),
#         ("Tottenham Hotspur", "🇬🇧"),
#         ("West Ham United", "🇬🇧"),
#         ("Wolverhampton Wanderers", "🇬🇧")
#     ],
    
#     "🇪🇸 La Liga": [
#         ("Alavés", "🇪🇸"),
#         ("Athletic Bilbao", "🇪🇸"),
#         ("Atlético Madrid", "🇪🇸"),
#         ("Barcelona", "🇪🇸"),
#         ("Cádiz", "🇪🇸"),
#         ("Celta Vigo", "🇪🇸"),
#         ("Elche", "🇪🇸"),
#         ("Espanyol", "🇪🇸"),
#         ("Getafe", "🇪🇸"),
#         ("Girona", "🇪🇸"),
#         ("Real Madrid", "🇪🇸"),
#         ("Real Sociedad", "🇪🇸"),
#         ("Sevilla", "🇪🇸"),
#         ("Valencia", "🇪🇸"),
#         ("Villarreal", "🇪🇸")
#     ],
    
#     "🇮🇹 Serie A": [
#         ("Atalanta", "🇮🇹"),
#         ("Bologna", "🇮🇹"),
#         ("Cremonese", "🇮🇹"),
#         ("Empoli", "🇮🇹"),
#         ("Fiorentina", "🇮🇹"),
#         ("Hellas Verona", "🇮🇹"),
#         ("Inter Milan", "🇮🇹"),
#         ("Juventus", "🇮🇹"),
#         ("Lazio", "🇮🇹"),
#         ("Lecce", "🇮🇹"),
#         ("Milan", "🇮🇹"),
#         ("Monza", "🇮🇹"),
#         ("Napoli", "🇮🇹"),
#         ("Roma", "🇮🇹"),
#         ("Sassuolo", "🇮🇹"),
#         ("Spezia", "🇮🇹"),
#         ("Torino", "🇮🇹"),
#         ("Udinese", "🇮🇹")
#     ],
    
#     "🇩🇪 Bundesliga": [
#         ("Augsburg", "🇩🇪"),
#         ("Bayer Leverkusen", "🇩🇪"),
#         ("Bayern Munich", "🇩🇪"),
#         ("Borussia Dortmund", "🇩🇪"),
#         ("Borussia Mönchengladbach", "🇩🇪"),
#         ("Eintracht Frankfurt", "🇩🇪"),
#         ("Freiburg", "🇩🇪"),
#         ("Hannover", "🇩🇪"),
#         ("Hoffenheim", "🇩🇪"),
#         ("Mainz", "🇩🇪"),
#         ("RB Leipzig", "🇩🇪"),
#         ("Union Berlin", "🇩🇪"),
#         ("VfL Wolfsburg", "🇩🇪")
#     ],
    
#     "🇫🇷 Ligue 1": [
#         ("Ajaccio", "🇫🇷"),
#         ("Angers", "🇫🇷"),
#         ("Auxerre", "🇫🇷"),
#         ("Brest", "🇫🇷"),
#         ("Clermont", "🇫🇷"),
#         ("Lorient", "🇫🇷"),
#         ("Lille", "🇫🇷"),
#         ("Lens", "🇫🇷"),
#         ("Lyon", "🇫🇷"),
#         ("Marseille", "🇫🇷"),
#         ("Monaco", "🇫🇷"),
#         ("Montpellier", "🇫🇷"),
#         ("Nantes", "🇫🇷"),
#         ("Nice", "🇫🇷"),
#         ("Paris Saint-Germain", "🇫🇷"),
#         ("Reims", "🇫🇷"),
#         ("Rennes", "🇫🇷"),
#         ("Strasbourg", "🇫🇷"),
#         ("Troyes", "🇫🇷"),
#         ("Toulouse", "🇫🇷")
#     ]
# }

# RARITY_CHOICES =[
#     ('Silver')
#     ('Bronze')
#     ('Common')
#     ('TEAM OF THE WEEK')
#     ('TOTS CHAMPIONS')
#     ('TEAM OF THE SEASON')
#     ('FUTTIES')
#     ('SHAPESHIFTERS')
#     ('ICON')
#     ('TOTS HONOURABLE MENTIONS')
#     ('FUT BIRTHDAY')
#     ('WINTER WILDCARDS')
#     ('UT HEROES')
#     ('NUMEROFUT')
#     ('FUTURE STARS')
#     ('TOTAL RUSH')
#     ('FUTTIES ICON')
#     ('SQUAD FOUNDATIONS')
#     ('TRAILBLAZERS')
#     ('FLASHBACK PLAYER')
#     ('FANSTASY FC')
#     ('FUT IMMORTALS ICON')
#     ('THUNDERSTRUCK')
#     ('WEURO PATH TO GLORY')
#     ('GLOBETROTTERS')
#     ('CENTURIONS')
#     ('UCL ROAD TO THE FINAL')
#     ('GRASSROOT GREATS')
#     ('ULTIMATE SUCCESSION')
#     ('WORLD TOUR')
#     ('UCL ROAD TO THE KNOCKOUTS')
#     ('FUTTIES HERO')
#     ('TOTY HONOURABLE MENTIONS')
#     ('TRACK STARS')
#     ('TEAM OF THE YEAR')
#     ('SHAPSHIFTER ICON')
#     ('UEFA EUROPA LEAGUE RTTF')
#     ('WINTER WILDCARDS ICON')
#     ('UCL DREAMCHASERS')
#     ('FUTURE STARS ICON')
#     ('WINTER WILDCARDS HERO')
#     ('FUT BIRTHDAY HERO')
#     ('UEFA CONFERENCE LEAGUE RTTF')
#     ('THUNDERSTRUCK')
#     ('SHOWDOWN PLUS')
#     ('STAR PERFORMER')
#     ('FANTASY FC HERO')
#     ('CHAMPION MASTERY')
#     ('SQUAD BATTLES MASTERY')
#     ('RIVALS MASTERY')
#     ('END OF AN ERA')
#     ('FUTURE STARS EVOLUTION')
#     ('PRIME HERO')
#     ('SHAPESHIFTER HERO')
#     ('TOTY ICON')
#     ('ON THIS DAY ICON')
#     ('CENTURIONS ICON ')
#     ('TRACK STARS HERO')
#     ('FUT BIRTHDAY ICON')
#     ('FUT IMMORTALS HERO')
#     ('ULTIMATE SUCCESSION ICON')
#     ('WINTER CHAMPIONS')
#     ('DREAMCHASER HERO')
#     ('MOMENTS')
#     ('PRIME HERO')
#     ('GREATS OF THE GAME HERO')
#     ('GREATS OF THE GAME ICON')
#     ('UECL DREAMCHASERS')
# ]

# class FIFA_CARD(models.Model):
#     Rating = models.PositiveIntegerField(min_length = 1, max_length = 99)
#     Position = models.CharField(choices = POSITION_CHOICES)
#     Nation = models.CharField( choices = NATIONS_CHOICES)
#     Club = models.CharField( choices = CLUB_CHOICES)
#     Name = models.CharField(max_length = 20)
#     Pace = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Shooting = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Passing = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Dribbling = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Defending = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Physicality = models.PositiveIntegerField(min_lenth = 1, max_length = 99)
#     Player_Image = models.URLField(blank= True, max_length = 500, null=True)
#     Card_Rarity = models.CharField(max_length = 10 , choices = RARITY_CHOICES)

#     class Meta:
#         db_table = "card"

# class CARD_RARITY(models.Model):
#     Name = models.CharField(max_length = 10 , choices = RARITY_CHOICES)
#     image_url = models.TextField(max_length=500)

    


from django.db import models


class Nation(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5) 

    def __str__(self):
        return f"{self.flag} {self.name}"


class League(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.flag} {self.name}"


class Club(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=5)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name="clubs")

    def __str__(self):
        return f"{self.flag} {self.name} ({self.league.name})"


class Position(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code} - {self.name}"


class CardRarity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    background_image = models.ImageField(upload_to="card_backgrounds/")

    def __str__(self):
        return self.name


class PlayerCard(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    nation = models.ForeignKey(Nation, on_delete=models.SET_NULL, null=True)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    rarity = models.ForeignKey(CardRarity, on_delete=models.SET_NULL, null=True)
    player_image = models.ImageField(upload_to="player_images/")

    # Player states
    pace = models.PositiveIntegerField()
    shooting = models.PositiveIntegerField()
    passing = models.PositiveIntegerField()
    dribbling = models.PositiveIntegerField()
    defending = models.PositiveIntegerField()
    physicality = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.rating})"
