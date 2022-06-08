import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TeamListComponent } from './team-list/team-list.component';
import { TeamDetailComponent } from './team-detail/team-detail.component';
import { GamePredictComponent } from './game-predict/game-predict.component';

const routes: Routes = [
  { path: 'teams', component: TeamListComponent},
  { path: 'team/:id', component: TeamDetailComponent},
  { path: 'predict', component: GamePredictComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
