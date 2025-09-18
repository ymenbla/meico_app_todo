import { Component } from '@angular/core';
import { MatTableDataSource,  MatTableModule } from '@angular/material/table';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { RouterModule } from '@angular/router';
import { Router } from '@angular/router';
import { DatePipe } from '@angular/common';

import { TodoService } from '../todo.service';
import { Task } from '../todo.model';

@Component({
  selector: 'app-todo-list',
  standalone: true,
  imports: [
    MatTableModule, MatChipsModule, MatIconModule,
    MatButtonModule, RouterModule, MatCardModule, DatePipe
  ],
  templateUrl: './todo-list.component.html',
  styleUrl: './todo-list.component.scss'
})
export class TodoListComponent {
  displayedColumns: string[] = ['title', 'description', 'task_status', 'created_at', 'actions'];
  dataSource = new MatTableDataSource<Task>([]);

  constructor(private todoService: TodoService, private router: Router) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    this.todoService.getTasks().subscribe(tasks => {
      this.dataSource.data = tasks;
    });
  }

  deleteTask(id: number) {
    this.todoService.deleteTask(id).subscribe(() => {
      this.dataSource.data = this.dataSource.data.filter(t => t.id !== id);
    });
  }

  editTask(id: number) {
    this.router.navigate(['/todo/edit', id]);
  }
}
