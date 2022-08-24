import { Component, ChangeDetectorRef, OnDestroy, OnInit, HostListener } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';
import { AgGridAngular } from 'ag-grid-angular';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnDestroy {
  mobileQuery: MediaQueryList;
  showFiller = false;
  width: any;
  title = "Hello";

  mobile_size: boolean;
  menu_open = false;
  fillerNav = Array.from({length: 50}, (_, i) => `Nav Item ${i + 1}`);


  private _mobileQueryListener: () => void;

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
    this.width = window.innerWidth;
    if (this.width > 880) {
      this.mobile_size = false;
    } else {
      this.mobile_size = true;
    }
  }

  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }

  mobileNavClick() {
    this.menu_open = !this.menu_open;
    var p_header = document.getElementById('primaryHeader')
    p_header?.toggleAttribute('data-overlay')

  }
  
  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
    this.width = window.innerWidth;
    if (this.width > 880) {
      this.mobile_size = false;
    } else {
      this.mobile_size = true;
    }
  }
}
