import { Routes } from '@angular/router';
import { authGuard } from './core/auth.guard';
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';

export const routes: Routes = [
  { path: 'login', loadComponent: () => import('./features/auth/login/login.component').then(m => m.LoginComponent) },
  { path: 'register', loadComponent: () => import('./features/auth/register/register.component').then(m => m.RegisterComponent) },

  {
    path: '',
    component: MainLayoutComponent,
    canActivate: [authGuard],
    children: [
      {
        path: 'todo', loadComponent: () => import('./pages/todo/todo-list/todo-list.component')
        .then(m => m.TodoListComponent)
      },
      {
        path: 'todo/new', loadComponent: () => import('./pages/todo/todo-form/todo-form.component')
        .then(m => m.TodoFormComponent)
      },
      {
        path: 'todo/edit/:id', loadComponent: () => import('./pages/todo/todo-form/todo-form.component')
        .then(m => m.TodoFormComponent)
      },
      { path: '', pathMatch: 'full', redirectTo: 'todo' }
    ]
  },

  { path: '**', redirectTo: '' }

];
