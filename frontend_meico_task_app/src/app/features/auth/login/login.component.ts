import { Component, inject, signal } from '@angular/core';
import { FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar';
import { AuthService } from '@core/auth.service';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    // RouterOutlet,
    RouterLink,
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatSnackBarModule,
    NgIf
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  private fb = inject(FormBuilder);
  private auth = inject(AuthService);
  private router = inject(Router);
  private snack = inject(MatSnackBar);

  loading = signal(false);

  form = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  });

  get f() { return this.form.controls; }

  onSubmit() {
    if (this.form.invalid) return;
    this.loading.set(true);

    this.auth.login(this.form.value as any).subscribe({
      next: () => {
        this.snack.open('Login exitoso', 'OK', { duration: 2000 });
        this.router.navigateByUrl('/'); // va al layout principal
      },
      error: () => {
        this.snack.open('Credenciales inválidas', 'Cerrar', { duration: 3000 });
        this.loading.set(false)
      },
      complete: () => this.loading.set(false)
    });
  }
}
