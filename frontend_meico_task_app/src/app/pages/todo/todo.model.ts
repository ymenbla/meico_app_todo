export interface Task {
  id: number;
  title: string;
  description: string;
  task_status: 'pendiente' | 'completado';
  created_at: string;
}
