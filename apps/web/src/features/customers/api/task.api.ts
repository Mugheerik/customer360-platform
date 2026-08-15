import { api } from "@/lib/api/client";

import type {
  Task,
  TaskCreate,
  TaskUpdate,
} from "../types/task.types";

export const TaskService = {
  async getCustomerTasks(
    customerId: string,
  ): Promise<Task[]> {
    const response = await api.get<Task[]>(
      `/customers/${customerId}/tasks`,
    );

    return response.data;
  },

  async createTask(
    customerId: string,
    data: TaskCreate,
  ): Promise<Task> {
    const response = await api.post<Task>(
      `/customers/${customerId}/tasks`,
      data,
    );

    return response.data;
  },

  async updateTask(
    customerId: string,
    taskId: string,
    data: TaskUpdate,
  ): Promise<Task> {
    const response = await api.patch<Task>(
      `/customers/${customerId}/tasks/${taskId}`,
      data,
    );

    return response.data;
  },

  async deleteTask(
    customerId: string,
    taskId: string,
  ): Promise<void> {
    await api.delete(
      `/customers/${customerId}/tasks/${taskId}`,
    );
  },
};