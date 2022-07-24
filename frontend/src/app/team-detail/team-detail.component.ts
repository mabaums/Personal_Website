import { Component, OnInit, ViewChild } from '@angular/core';
import { CellClickedEvent, ColDef, GridReadyEvent } from 'ag-grid-community';
import { AgGridAngular } from 'ag-grid-angular';
import { Observable } from 'rxjs';
import { ClientService, Team } from 'api-swagger-library';
import { Router } from '@angular/router';
import { TEMPORARY_NAME } from '@angular/compiler/src/render3/view/util';
@Component({
  selector: 'app-team-detail',
  templateUrl: './team-detail.component.html',
  styleUrls: ['./team-detail.component.css'],
  providers: [ClientService]
})
export class TeamDetailComponent implements OnInit {

  name_to_id: { [key: string]: number } = { 'Manchester City': 50, 'Liverpool': 40, 'Chelsea': 49, 'Tottenham': 47, 'Arsenal': 42, 'Manchester United': 33, 'West Ham': 48, 'Leicester': 46, 'Brighton': 51, 'Wolves': 39, 'Newcastle': 34, 'Crystal Palace': 52, 'Brentford': 55, 'Aston Villa': 66, 'Southampton': 41, 'Everton': 45, 'Leeds': 63, 'Burnley': 44, 'Watford': 38, 'Norwich': 71 };
  team_name: string | undefined;

  constructor(private clientApi: ClientService, private router: Router) {
    this.team = {} as Team;
    if (decodeURIComponent(this.router.url).split('/').pop()) {
      this.team_name = decodeURIComponent(this.router.url).split('/').pop();
    } else { }

  }
  team: Team;
  ngOnInit(): void {

    console.log()
    this.clientApi.getTeam(this.name_to_id[this.team_name!]).subscribe(body => {
      this.team = body;
    }
    )
  }



  columnDefs = [{ field: "make" }, { field: "model" }, { field: "price" }];

  rowData = [
    { make: "Toyota", model: "Celica", price: 35000 },
    { make: "Ford", model: "Mondeo", price: 32000 },
    { make: "Porsche", model: "Boxter", price: 72000 }
  ];
}
