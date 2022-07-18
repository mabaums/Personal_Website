import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { ClientService } from 'api-swagger-library/api/client.service'
import { Team } from 'api-swagger-library';
import { MatTable, MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { animate, state, style, transition, trigger } from '@angular/animations';

@Component({
  selector: 'app-team-list',
  templateUrl: './team-list.component.html',
  styleUrls: ['./team-list.component.css'],
  providers: [ClientService],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})

export class TeamListComponent implements OnInit{

  teams: Team[];
  dataSource: MatTableDataSource<Team>;
  expandedTeam: Team | null | undefined;
  @ViewChild(MatSort) sort: MatSort = new MatSort;

  public options: any;


  constructor(private clientApi: ClientService) { 
    this.teams = [];
    this.dataSource = new MatTableDataSource(this.teams);

  }



  displayedColumns: string[] = ['Rk', 'Squad', 'GD', 'MP', 'Pts'];
  ngOnInit(): void {}
  

}
