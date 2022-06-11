import { Component, OnInit } from '@angular/core';
import { ICellRendererAngularComp } from 'ag-grid-angular';
import { ICellRendererParams } from 'ag-grid-community';

@Component({
  selector: 'app-team-cell',
  template: `
    <p>
      <img style="max-width: 15px;" src="{{value.logo}}"> <a routerLink="/team/{{value.name}}">{{value.name}}</a>
    </p>
  `,
  styles: [
  ]
})
export class TeamCellComponent implements OnInit, ICellRendererAngularComp {

  constructor() { }

  value: any;

  refresh(params: ICellRendererParams): boolean {
    return false;
  }
  agInit(params: ICellRendererParams): void {
    this.value = params.value;
  }

  

  ngOnInit(): void {
  }

}
