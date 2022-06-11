import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TeamCellComponent } from './team-cell.component';

describe('TeamCellComponent', () => {
  let component: TeamCellComponent;
  let fixture: ComponentFixture<TeamCellComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TeamCellComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TeamCellComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
