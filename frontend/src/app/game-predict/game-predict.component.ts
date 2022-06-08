import { Component, OnInit } from '@angular/core';
import { MatFormField } from '@angular/material/form-field';
import { ClientService, Game } from 'api-swagger-library';

@Component({
  selector: 'app-game-predict',
  templateUrl: './game-predict.component.html',
  styleUrls: ['./game-predict.component.css'],
  providers: [ClientService]
})
export class GamePredictComponent implements OnInit {

  constructor(private clientApi: ClientService) { }
  game: Game | undefined;
  ngOnInit(): void {
  }

  predict(homeId: number, awayId: number) {
    this.clientApi.predictGame(1, 1).subscribe(
      body => {
        this.game = body as Game;
        console.log(this.game);
        console.log(this.game.goals_home)
      }
    )
  }

}
