import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";

import { TaskService } from "../api/task.api";
import TaskForm from "./TaskForm";

import type {
  Task,
  TaskStatus,
} from "../types/task.types";

type TasksSectionProps = {
  customerId: string;
};

export default function TasksSection({
  customerId,
}: TasksSectionProps) {
  const queryClient = useQueryClient();

  const tasksQuery = useQuery({
    queryKey: ["customers", customerId, "tasks"],
    queryFn: () =>
      TaskService.getCustomerTasks(customerId),
  });

  const createTaskMutation = useMutation({
    mutationFn: TaskService.createTask.bind(
      null,
      customerId,
    ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "tasks",
        ],
      });

      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "timeline",
        ],
      });
    },
  });

  const updateTaskMutation = useMutation({
    mutationFn: ({
      taskId,
      status,
    }: {
      taskId: string;
      status: TaskStatus;
    }) =>
      TaskService.updateTask(
        customerId,
        taskId,
        { status },
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "tasks",
        ],
      });

      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "timeline",
        ],
      });
    },
  });

  const deleteTaskMutation = useMutation({
    mutationFn: (taskId: string) =>
      TaskService.deleteTask(
        customerId,
        taskId,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "tasks",
        ],
      });

      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "timeline",
        ],
      });
    },
  });

  const handleStatusChange = (
    task: Task,
    status: TaskStatus,
  ) => {
    updateTaskMutation.mutate({
      taskId: task.id,
      status,
    });
  };

  return (
    <Card className="p-6">
      <div>
        <h2 className="text-lg font-semibold text-text">
          Tasks
        </h2>

        <p className="mt-1 text-sm text-text-secondary">
          Manage work associated with this customer.
        </p>
      </div>

      <div className="mt-6">
        <TaskForm
          onSubmit={(data) =>
            createTaskMutation.mutate(data)
          }
          isSubmitting={
            createTaskMutation.isPending
          }
        />
      </div>

      {createTaskMutation.isError && (
        <p className="mt-3 text-sm text-danger">
          Unable to create task.
        </p>
      )}

      <div className="mt-8 space-y-4">
        {tasksQuery.isLoading && (
          <p className="text-sm text-text-secondary">
            Loading tasks...
          </p>
        )}

        {tasksQuery.isError && (
          <p className="text-sm text-danger">
            Unable to load tasks.
          </p>
        )}

        {!tasksQuery.isLoading &&
          !tasksQuery.isError &&
          tasksQuery.data?.length === 0 && (
            <p className="text-sm text-text-secondary">
              No tasks yet.
            </p>
          )}

        {tasksQuery.data?.map((task) => (
          <div
            key={task.id}
            className="rounded-lg border border-border p-4"
          >
            <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
              <div>
                <h3 className="font-medium text-text">
                  {task.title}
                </h3>

                {task.description && (
                  <p className="mt-1 text-sm text-text-secondary">
                    {task.description}
                  </p>
                )}
              </div>

              <span className="text-xs font-medium uppercase text-text-secondary">
                {task.priority}
              </span>
            </div>

            <div className="mt-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <select
                value={task.status}
                onChange={(event) =>
                  handleStatusChange(
                    task,
                    event.target.value as TaskStatus,
                  )
                }
                className="rounded-lg border border-border bg-background px-3 py-2 text-sm text-text"
                disabled={
                  updateTaskMutation.isPending
                }
              >
                <option value="todo">
                  Todo
                </option>

                <option value="in_progress">
                  In Progress
                </option>

                <option value="done">
                  Done
                </option>
              </select>

              <Button
                type="button"
                variant="secondary"
                onClick={() =>
                  deleteTaskMutation.mutate(
                    task.id,
                  )
                }
                disabled={
                  deleteTaskMutation.isPending
                }
              >
                Delete
              </Button>
            </div>

            <p className="mt-3 text-xs text-text-secondary">
              Created{" "}
              {new Date(
                task.created_at,
              ).toLocaleString()}
            </p>
          </div>
        ))}
      </div>
    </Card>
  );
}