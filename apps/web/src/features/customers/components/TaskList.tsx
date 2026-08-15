import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";

import { TaskService } from "../api/task.api";
import type { Task, TaskStatus } from "../types/task.types";

type TaskListProps = {
  customerId: string;
};

const statusLabels: Record<TaskStatus, string> = {
  todo: "To Do",
  in_progress: "In Progress",
  done: "Done",
};

export default function TaskList({
  customerId,
}: TaskListProps) {
  const queryClient = useQueryClient();

  const [deletingTaskId, setDeletingTaskId] = useState<
    string | null
  >(null);

  const tasksQuery = useQuery({
    queryKey: ["customers", customerId, "tasks"],
    queryFn: () =>
      TaskService.getCustomerTasks(customerId),
    enabled: Boolean(customerId),
  });

  const deleteTaskMutation = useMutation({
    mutationFn: (taskId: string) =>
      TaskService.deleteTask(customerId, taskId),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: ["customers", customerId, "tasks"],
      });

      await queryClient.invalidateQueries({
        queryKey: ["customers", customerId, "timeline"],
      });

      setDeletingTaskId(null);
    },

    onError: () => {
      setDeletingTaskId(null);
    },
  });

  const handleDelete = (taskId: string) => {
    setDeletingTaskId(taskId);
    deleteTaskMutation.mutate(taskId);
  };

  if (tasksQuery.isLoading) {
    return (
      <Card className="p-6">
        <p className="text-sm text-text-secondary">
          Loading tasks...
        </p>
      </Card>
    );
  }

  if (tasksQuery.isError) {
    return (
      <Card className="p-6">
        <p className="text-sm text-danger">
          Unable to load tasks.
        </p>
      </Card>
    );
  }

  const tasks = tasksQuery.data ?? [];

  return (
    <Card className="p-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-lg font-semibold text-text">
            Tasks
          </h2>

          <p className="mt-1 text-sm text-text-secondary">
            Tasks associated with this customer.
          </p>
        </div>
      </div>

      {deleteTaskMutation.isError && (
        <div className="mt-4 rounded-lg border border-red-200 bg-red-50 p-4">
          <p className="text-sm text-danger">
            Unable to delete the task. Please try again.
          </p>
        </div>
      )}

      {tasks.length === 0 ? (
        <div className="mt-6 rounded-lg border border-border p-6 text-center">
          <p className="text-sm text-text-secondary">
            No tasks have been created for this customer.
          </p>
        </div>
      ) : (
        <div className="mt-6 divide-y divide-border">
          {tasks.map((task: Task) => (
            <div
              key={task.id}
              className="py-5 first:pt-0 last:pb-0"
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div className="min-w-0">
                  <h3 className="font-medium text-text">
                    {task.title}
                  </h3>

                  {task.description && (
                    <p className="mt-2 text-sm text-text-secondary">
                      {task.description}
                    </p>
                  )}

                  <div className="mt-3 flex flex-wrap gap-2 text-xs">
                    <span className="rounded-full bg-surface px-2.5 py-1 text-text-secondary">
                      {statusLabels[task.status]}
                    </span>

                    <span className="rounded-full bg-surface px-2.5 py-1 capitalize text-text-secondary">
                      {task.priority}
                    </span>
                  </div>
                </div>

                <Button
                  variant="secondary"
                  type="button"
                  onClick={() => handleDelete(task.id)}
                  disabled={deletingTaskId === task.id}
                >
                  {deletingTaskId === task.id
                    ? "Deleting..."
                    : "Delete"}
                </Button>
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}