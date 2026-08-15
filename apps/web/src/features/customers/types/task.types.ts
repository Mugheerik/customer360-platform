export type TaskStatus =
  | "todo"
  | "in_progress"
  | "done";

export type TaskPriority =
  | "low"
  | "medium"
  | "high";

export type Task = {
  id: string;
  customer_id: string;
  assigned_to: string | null;
  title: string;
  description: string | null;
  status: TaskStatus;
  priority: TaskPriority;
  created_at: string;
  updated_at: string;
};

export type TaskCreate = {
  title: string;
  description?: string | null;
  assigned_to?: string | null;
  priority?: TaskPriority;
};

export type TaskUpdate = {
  title?: string | null;
  description?: string | null;
  assigned_to?: string | null;
  status?: TaskStatus | null;
  priority?: TaskPriority | null;
};