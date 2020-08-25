import csv
import players as MLBPlayers
import statistics
from datetime import datetime as dt


HIGHEST_SALARIES_THRESHOLD = 125

def _save_result(offer, players, clean_players, top_players):
    date_str = dt.now().strftime("%m-%d-%Y-%H-%M-%S")

    with open(f'all_players_{date_str}.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(MLBPlayers.Player.CSV_HEADER)
        csv_writer.writerows(x.to_csv_row() for x in players)

    with open(f'top_players_{date_str}.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(MLBPlayers.Player.CSV_HEADER)
        csv_writer.writerows(x.to_csv_row() for x in top_players)

    with open(f'results_{date_str}.txt', 'w') as f:
        f.writelines(
            '\n'.join(
                [
                    f'The qualifying offer is {offer}',
                    f'There were {len(clean_players)} salaries that were used out of {len(players)} total salaries.',
                    "Please see the attached csv files to see the top players and reasons why certain players' salaries were not used",
                ]
            )
        )

def _run():
    players = MLBPlayers.fetch()
    clean_players = [x for x in players if x.salary_status == MLBPlayers.SalaryStatus.GOOD]
    top_players = sorted(clean_players, key=lambda x: x.salary, reverse=True)[:HIGHEST_SALARIES_THRESHOLD]

    for top_player in top_players:
        top_player.is_top_player = True

    mean_salary = statistics.mean(x.salary for x in top_players)
    offer = "${:,.2f}".format(mean_salary)

    _save_result(offer, players, clean_players, top_players)


if __name__ == '__main__':
    print('Starting.')
    _run()
    print('Finished. Please check results.txt file.')