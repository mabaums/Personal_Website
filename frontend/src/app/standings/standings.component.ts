import { Component, OnInit } from '@angular/core';
import { ClientService } from 'api-swagger-library';
import { ColDef, GridReadyEvent } from 'ag-grid-community';
import { AgGridAngular } from 'ag-grid-angular';
import { GridApi, ColumnApi } from 'ag-grid-community';
import { CellRendererComponent } from 'ag-grid-community/dist/lib/components/framework/componentTypes';
import { TeamCellComponent } from '../team-cell/team-cell.component';
@Component({
  selector: 'app-standings',
  templateUrl: './standings.component.html',
  styleUrls: ['./standings.component.css'],
  providers: [ClientService]
})
export class StandingsComponent implements OnInit {

  standings: any | undefined;
  public style: any;
  private gridApi!: GridApi;
  private gridColumnApi!: ColumnApi;

  constructor(private clientApi: ClientService) { }
  columnDefs = [
    { field: 'rank' },
    { field: 'team_name'}, // TODO: Change back to cell renderer component with passing logo and change field title?
    { field: 'points' },
    { field: 'goalsDiff'},
    { field: 'form'},
    { field: 'description'},


  ];

  ngOnInit(): void {

    this.clientApi.getStanding().subscribe(
      body => {
        this.standings = body; // Results in array of standings with various info? could probably change some stuff
      }
    )
  }

  onGridReady(params: GridReadyEvent) {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;

    this.gridApi.setDomLayout('autoHeight');

    const allColumnIds: string[] = [];
    this.gridColumnApi.getAllColumns()!.forEach((column) => {
      allColumnIds.push(column.getId());
    });
    this.gridColumnApi.autoSizeColumns(allColumnIds);
  }


  
}
