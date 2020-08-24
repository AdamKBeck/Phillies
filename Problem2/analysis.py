import players as MLBPlayers


if __name__ == '__main__':
    players = MLBPlayers.fetch()
    clean_players = [x for x in players if x.salary_status == MLBPlayers.SalaryStatus.GOOD]
    print(len(clean_players))
