import { Component, OnInit } from '@angular/core';
import { MatFormField } from '@angular/material/form-field';
import { ClientService, PredictedGame } from 'api-swagger-library';
import { MatTableDataSource } from '@angular/material/table';

interface GameWeek {
  value: number;
  viewValue: string;
}

interface Algo {
  value: number;
  viewValue: string;
}

interface Team {
  value: number;
  viewValue: string;
}

@Component({
  selector: 'app-game-predict',
  templateUrl: './game-predict.component.html',
  styleUrls: ['./game-predict.component.css'],
  providers: [ClientService]
})


export class GamePredictComponent implements OnInit {

  predictedRound: any | undefined;
  selectedAlgo: Algo;
  isLoading: boolean = false;
  selectedWeek = 10;
  gameWeeks: GameWeek[] = []
  selectedHomeTeam = 1;
  selectedAwayTeam = 2;
  teams: Team[] = [
    { value: 1, viewValue: 'Chelsea FC' },
    { value: 2, viewValue: 'Manchester City' }
  ]

  algos: Algo[] = [
    {value: 1, viewValue: 'CNN (Convolutional Neural Network)'},
    {value: 2, viewValue: 'RNN (Random Neural Network)'},
    {value: 3, viewValue: 'LSTM (Limited Time Sale)'},
    {value: 4, viewValue: 'FLDR (FDR)'}
  ]


  constructor(private clientApi: ClientService) {
    for (let i = 5; i < 39; i++) {
      this.gameWeeks.push({ value: i, viewValue: "Game Week ".concat(i.toString()) })
    }
    this.selectedAlgo = this.algos[0];

  }
  game: PredictedGame | undefined;
  ngOnInit(): void {

  }

  predictRound(roundID: number) {
    this.isLoading = true;
    this.predictedRound = undefined;
    this.clientApi.predictRound(roundID).subscribe(body => {
      this.predictedRound = body;
      this.isLoading = false;
    })
  }
  predict(homeId: number, awayId: number) {
    this.isLoading = true;
    this.clientApi.predictGame(homeId, awayId).subscribe(
      body => {
        this.game = body as PredictedGame;
        this.isLoading = false;
      }
    )
  }

  onSelect(algo: Algo) {
    this.selectedAlgo = algo;
  }

  displayedColumns: string[] = ['Home Team', 'Away Team', 'Predicted GD', 'Predicted Result',
   'Actual GD', 'Full Time Result'];

}
