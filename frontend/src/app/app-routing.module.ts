import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TeamListComponent } from './team-list/team-list.component';
import { TeamDetailComponent } from './team-detail/team-detail.component';
import { GamePredictComponent } from './game-predict/game-predict.component';
import { StandingsComponent } from './standings/standings.component';
const routes: Routes = [
  { path: 'teams', component: TeamListComponent},
  { path: 'team/:id', component: TeamDetailComponent},
  { path: 'predict', component: GamePredictComponent},
  { path: 'standings', component: StandingsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
