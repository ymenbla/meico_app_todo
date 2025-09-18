import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatSelectModule } from "@angular/material/select";
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { TodoService } from '../todo.service';
import { Task } from '../todo.model';

@Component({
  selector: 'app-todo-form',
  standalone: true,
  imports: [
    MatFormFieldModule, MatInputModule ,
    MatSelectModule, FormsModule, ReactiveFormsModule,
    MatCardModule, MatToolbarModule, MatIconModule, MatButtonModule,
    RouterModule
  ],
  templateUrl: './todo-form.component.html',
  styleUrl: './todo-form.component.scss'
})
export class TodoFormComponent implements OnInit {
  form!: FormGroup;
  taskId!: number | null;
  taskCurrent!: Task;

  constructor(
    private fb: FormBuilder,
    private todoService: TodoService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      title: ['', Validators.required],
      description: ['', Validators.required],
      task_status: ['pendiente']
    });

    this.taskId = Number(this.route.snapshot.paramMap.get('id'));
    if (this.taskId) {
      this.todoService.getTasks().subscribe(tasks => {
        const task = tasks.find(t => t.id === this.taskId);
        if (task) {
          this.form.patchValue(task);
          this.taskCurrent = task;
        }
      });
    }
  }

  save() {
    if (this.form.invalid) return;

    if (this.taskId) {
      let form = this.form.value;
      let taskupdated = this.taskCurrent;

      taskupdated.title = form.title;
      taskupdated.description = form.description;
      taskupdated.task_status = form.task_status;

      this.todoService.updateTask(this.taskId, taskupdated).subscribe(() => {
        this.router.navigate(['/todo']);
      });
    } else {
      this.todoService.createTask(this.form.value).subscribe(() => {
        this.router.navigate(['/todo']);
      });
    }
  }

  goBack() {
    this.router.navigate(['/todo']); // volver a la lista de tareas
  }
}
