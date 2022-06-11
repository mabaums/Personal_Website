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

export class TeamListComponent implements OnInit, AfterViewInit{

  teams: Team[];
  dataSource: MatTableDataSource<Team>;
  expandedTeam: Team | null | undefined;
  @ViewChild(MatSort) sort: MatSort = new MatSort;

  public options: any;


  constructor(private clientApi: ClientService) { 
    this.teams = [];
    this.dataSource = new MatTableDataSource(this.teams);

    this.options = {
      theme: 'ag-default-dark',
      autoSize:true,
      title: {
        text: 'Season Performance'
      },
      subtitle: {
        text: 'Points by match Day'
      },
      data: [
        {
          match_day: '1',
          Points: 3,
        },
        {
          match_day: '2',
          Points: 6
        },
        {
          match_day: '3',
          Points: 9
        },
        {
          match_day: '4',
          Points: 9
        },
        {
          match_day: '5',
          Points: 9
        },
        {
          match_day: '6',
          Points: 9
        },
        {
          match_day: '7',
          Points: 9
        }
      ],
      series: [{
          xKey: 'match_day',
          yKey: 'Points',
      }],
  };

  }
  ngAfterViewInit(): void {
    this.clientApi.getTeams().subscribe(
      body => {
        this.teams = body;
        this.dataSource = new MatTableDataSource(this.teams);
        this.dataSource.sort = this.sort;
      }
    )

    this.clientApi.getStanding().subscribe(
      body => {
        console.log(body);
      }
    )

  }



  displayedColumns: string[] = ['Rk', 'Squad', 'GD', 'MP', 'Pts'];
  ngOnInit(): void {}
  

}
