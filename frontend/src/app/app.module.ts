import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TeamListComponent } from './team-list/team-list.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table';
import { MatToolbarModule} from '@angular/material/toolbar';
import { MatSortModule } from '@angular/material/sort';
import { TeamDetailComponent } from './team-detail/team-detail.component';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule} from '@angular/material/icon';
import { MatSidenavModule} from '@angular/material/sidenav';
import {MatListModule} from '@angular/material/list';
import { AgGridModule } from 'ag-grid-angular';
import { FormsModule } from '@angular/forms';
import { AgChartsAngularModule } from 'ag-charts-angular';
import { GamePredictComponent } from './game-predict/game-predict.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { StandingsComponent } from './standings/standings.component';
import { TeamCellComponent } from './team-cell/team-cell.component';
import { MatSelectModule } from '@angular/material/select';
import { TeamCardComponent } from './team-card/team-card.component';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { HomePageComponent } from './home-page/home-page.component';
import { environment } from 'src/environments/environment';
import { BASE_PATH } from 'api-swagger-library';

@NgModule({
  declarations: [
    AppComponent,
    TeamListComponent,
    TeamDetailComponent,
    GamePredictComponent,
    StandingsComponent,
    TeamCellComponent,
    TeamCardComponent,
    HomePageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatToolbarModule,
    MatSortModule,
    MatButtonModule,
    MatIconModule,
    MatSidenavModule,
    MatListModule,
    AgGridModule,
    FormsModule,
    AgChartsAngularModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatProgressBarModule
  ],
  providers: [{ provide: BASE_PATH, useValue: environment.API_BASE_PATH}],
  bootstrap: [AppComponent]
})
export class AppModule { }
