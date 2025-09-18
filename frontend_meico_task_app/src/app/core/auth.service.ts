import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, catchError, map, of, tap, throwError } from 'rxjs';
import { Router } from '@angular/router';
import { environment } from '@environments/environment';

type LoginDto = { email: string; password: string };
type RegisterDto = { username: string; password: string };
type LoginResponse = { access_token: string };

@Injectable({ providedIn: 'root' })
export class AuthService {
  private http = inject(HttpClient);
  private router = inject(Router);

  private _isAuth$ = new BehaviorSubject<boolean>(this.hasValidToken());
  isAuth$ = this._isAuth$.asObservable();

  private get storageKey() { return 'token'; }

  get token(): string | null {
    return localStorage.getItem(this.storageKey);
  }

  private set token(value: string | null) {
    if (value) localStorage.setItem(this.storageKey, value);
    else localStorage.removeItem(this.storageKey);
  }

  login(dto: LoginDto) {
    return this.http.post<LoginResponse>(`${environment.apiUrl}/token`, dto)
    .pipe(
      tap(res => {
        this.token = res.access_token;
        this._isAuth$.next(true);
      })
    );
  }

  register(dto: RegisterDto) {
    return this.http.post(`${environment.apiUrl}/register`, dto)
    .pipe(
      catchError(err => throwError(() => err))
    );
  }

  logout() {
    this.token = null;
    this._isAuth$.next(false);
    this.router.navigateByUrl('/login');
  }

  /** Valida exp del JWT */
  hasValidToken(): boolean {
    const t = localStorage.getItem(this.storageKey);
    if (!t) return false;
    try {
      const payload = JSON.parse(atob(t.split('.')[1] || ''));
      if (payload?.exp) {
        const nowSec = Math.floor(Date.now() / 1000);
        return payload.exp > nowSec;
      }
      return true;
    } catch {
      return true; // token presente pero no decodificable
    }
  }
}
