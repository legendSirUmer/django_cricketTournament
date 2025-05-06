from  .models import Player, Team

def populate_teams_and_players():
    # Define teams and their players
    teams_data = [
        {
            "team_name": "Adil Lions",
            "captain_contact": "42301-8054807-7",
            "players": [
                {"name": "Muhammad Adil", "enrollment": "02-111242-039", "cnic": "42301-8054807-7"},
                {"name": "Muhammad Ali", "enrollment": "02-111242-137", "cnic": "42301-8054807-7"},
                {"name": "Shaikh Saim", "enrollment": "02-111242-243", "cnic": "42301-8054807-7"},
                {"name": "Murtaza Mustafa", "enrollment": "02-111242-251", "cnic": "42301-8054807-7"},
                {"name": "Daniyal Anwar", "enrollment": "02-111242-067", "cnic": "42301-8054807-7"},
                {"name": "Mustafa Raza", "enrollment": "02-111241-095", "cnic": "42301-8054807-7"},
                {"name": "Saroosh", "enrollment": "02-111231-137", "cnic": "42301-8054807-7"},
                {"name": "Mohsin", "enrollment": "02-111231-119", "cnic": "42301-8054807-7"},
                {"name": "Hammad Asghar", "enrollment": "02-111231-121", "cnic": "42301-8054807-7"},
                {"name": "Marij Rehan", "enrollment": "02-111231-208", "cnic": "42301-8054807-7"},
                {"name": "Hammad Ali", "enrollment": "02-111231-260", "cnic": "42301-8054807-7"},
                {"name": "Rahim", "enrollment": "02-111242-017", "cnic": "42301-8054807-7"},
            ],
        },
        {
            "team_name": "KonTalha XI",
            "captain_contact": "42201-0930050-5",
            "players": [
                {"name": "Ebad", "enrollment": "02-134232-113", "cnic": "42201-0930050-5"},
                {"name": "Musharaf", "enrollment": "02-134242-031", "cnic": "42501-2732043-1"},
                {"name": "Abdul Basit", "enrollment": "02-235232-016", "cnic": "42101-5344143-3"},
                {"name": "Ali Hamza", "enrollment": "02-235232-003", "cnic": "42201-8400938-9"},
                {"name": "Talha", "enrollment": "02-134232-109", "cnic": "41304-1720087-7"},
                {"name": "Asad", "enrollment": "02-111212-082", "cnic": "42201-8826786-7"},
                {"name": "Hadi", "enrollment": "02-134232-010", "cnic": "42201-6758669-7"},
                {"name": "Hannan", "enrollment": "02-134232-059", "cnic": "4250150416843"},
                {"name": "Zyan", "enrollment": "02-134232-032", "cnic": "42201-8632388-1"},
                {"name": "Hammad", "enrollment": "02-134232-013", "cnic": "42101-6374489-7"},
                {"name": "Jawad", "enrollment": "05-171232-032", "cnic": "33201-0785829-1"},
                {"name": "Khubaib", "enrollment": "02-134232-083", "cnic": "42101-5353-603-9"},
                {"name": "Saim", "enrollment": "02-134231-022", "cnic": "42101-6920430-5"},
                {"name": "Moosa", "enrollment": "02-134232-026", "cnic": "42101-9716125-7"},
            ],
        },
        {
            "team_name": "Thunder Strikers",
            "captain_contact": "03182323467",
            "players": [
                {"name": "Muhammad Hassan", "enrollment": "02-235231-038", "cnic": "42101-7540572-1"},
                {"name": "Yasir Hussain", "enrollment": "02-235231-001", "cnic": "42201-9283371-3"},
                {"name": "Syed Qambar Ali Shah", "enrollment": "02-235231-006", "cnic": "42401-7171139-7"},
                {"name": "Arham Waqar", "enrollment": "02-235231-035", "cnic": "42201-2011560-9"},
                {"name": "Izhan Khan", "enrollment": "02-235231-045", "cnic": "42201-5260550-1"},
                {"name": "Hasnain Khalid", "enrollment": "02-134231-033", "cnic": "45302-6336933-9"},
                {"name": "Meerza Muhammad Wajih", "enrollment": "02-235231-031", "cnic": "42201-1168682-7"},
                {"name": "Huzaifa Ali", "enrollment": "02-235231-027", "cnic": "42101-4674925-7"},
                {"name": "Sarim Ali", "enrollment": "02-235231-052", "cnic": "34603-7493423-3"},
                {"name": "Muhammad Hammad Raza", "enrollment": "02-235231-036", "cnic": "34502-4146020-1"},
                {"name": "Muhammad Umer", "enrollment": "02-235231-012", "cnic": "42201-739344-9"},
                {"name": "Mustafa Warind", "enrollment": "02-235231-026", "cnic": "42201-4779733-3"},
                {"name": "Afazal", "enrollment": "02-235221-023", "cnic": "42201-8720694-7"},
                {"name": "Huzaifa Nadeem", "enrollment": "02-235231-032", "cnic": "42101-0943585-7"},
                {"name": "Syed Muhammad Abuzar Naqvi", "enrollment": "02-134232-045", "cnic": "42101-0943585-7"},
            ],
        },
        {
            "team_name": "MS Strikers",
            "captain_contact": "03342476146",
            "players": [
                {"name": "Muhammad Sobaan", "enrollment": "02-111241-136", "cnic": "4220153326855"},
                {"name": "Muhammad Mustafa", "enrollment": "02-135242-037", "cnic": "4250174582165"},
                {"name": "Anas Mujtaba", "enrollment": "02-239242-140", "cnic": "4220139104685"},
                {"name": "Hafeez Asif", "enrollment": "02-239251-099", "cnic": "4220170420409"},
                {"name": "Bilal Bhatti", "enrollment": "02-111232-332", "cnic": "4220177512577"},
                {"name": "Maaz Iftikhar", "enrollment": "02-135242-010", "cnic": "3610215196569"},
                {"name": "Arslan Riffat", "enrollment": "02-111221-030", "cnic": "3740262457939"},
                {"name": "Muhammad Fawad", "enrollment": "02-112222-039", "cnic": "4240130465725"},
                {"name": "Adnan", "enrollment": "02-116222-031", "cnic": "4250150466843"},
                {"name": "Talha", "enrollment": "02-350242-025", "cnic": "4250151510893"},
                {"name": "M Salman Raza", "enrollment": "02-111221-240", "cnic": "42201-9561682-3"},
            ],
        },
        {
            "team_name": "The Gladiators",
            "captain_contact": "+92 349 6503412",
            "players": [
                {"name": "Ali Ghouri", "enrollment": "02-112222-106", "cnic": "42201-1168541-7"},
                {"name": "Ehaan", "enrollment": "02-112222-036", "cnic": "42201-1168541-7"},
                {"name": "Hamza", "enrollment": "02-112222-025", "cnic": "42201-1168541-7"},
                {"name": "Saad", "enrollment": "02-112222-149", "cnic": "42201-1168541-7"},
                {"name": "Usama", "enrollment": "02-112231-127", "cnic": "42201-1168541-7"},
                {"name": "Haseeb", "enrollment": "02-112222-019", "cnic": "42201-1168541-7"},
                {"name": "Mudasir", "enrollment": "02-112222-038", "cnic": "42201-1168541-7"},
                {"name": "Sufyan", "enrollment": "02-112222-133", "cnic": "42201-1168541-7"},
                {"name": "Hamza Nasir", "enrollment": "02-112222-122", "cnic": "42201-1168541-7"},
                {"name": "M.Abdullah", "enrollment": "02-112222-124", "cnic": "42201-1168541-7"},
                {"name": "M.Yousuf", "enrollment": "02-112222-084", "cnic": "42201-1168541-7"},
                {"name": "M.Shyana", "enrollment": "02-112222-051", "cnic": "42201-1168541-7"},
                {"name": "Salman Shoqaut", "enrollment": "02-112222-037", "cnic": "42201-1168541-7"},
            ],
        },
        {
            "team_name": "Maritme Strikers",
            "captain_contact": "03378310874",
            "players": [
                {"name": "Jamshed Ali", "enrollment": "02-101232-020", "cnic": "44202-5879152-1"},
                {"name": "Hafiz Saifullah", "enrollment": "02-101232-016", "cnic": "42401-3989335-7"},
                {"name": "Taimoor Rashid", "enrollment": "02-101232-003", "cnic": "13011-0824281-5"},
                {"name": "Abdullah", "enrollment": "02-101232-006", "cnic": "42201-4278206-7"},
                {"name": "Noushad Khan", "enrollment": "02-101232-007", "cnic": "71502-7457752-7"},
                {"name": "Tabraiz Ahmed", "enrollment": "02-117221-036", "cnic": "55103-3713495-3"},
                {"name": "Yousuf", "enrollment": "02-102242-002", "cnic": "42101-3051964-1"},
                {"name": "Khurram", "enrollment": "02-102242-003", "cnic": "43201-3134883-9"},
                {"name": "Nabeel Iqbal", "enrollment": "02-101232-001", "cnic": "42201-6188329-3"},
                {"name": "Humayun Khan", "enrollment": "02-101242-001", "cnic": "42401-3512174-9"},
                {"name": "Talha Mansha", "enrollment": "02-101242-022", "cnic": "42201-4507265-1"},
            ],
        },
    ]

    # Populate teams and players
    for team_data in teams_data:
        team = Team.objects.create(name=team_data["team_name"])
        for player_data in team_data["players"]:
            player = Player.objects.create(
                name=player_data["name"],
                enrollment=player_data["enrollment"],
               
            )
            team.players.add(player)
        team.save()

    print("Teams and players have been populated successfully!")