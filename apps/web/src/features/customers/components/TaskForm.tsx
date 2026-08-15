import { useState } from "react";

import Button from "@/components/ui/button";
import type {
  TaskCreate,
  TaskPriority,
} from "../types/task.types";

type TaskFormProps = {
  onSubmit: (data: TaskCreate) => void;
  isSubmitting?: boolean;
};

export default function TaskForm({
  onSubmit,
  isSubmitting = false,
}: TaskFormProps) {
  const [title, setTitle] = useState("");
  const [description, setDescription] =
    useState("");
  const [priority, setPriority] =
    useState<TaskPriority>("medium");

  const handleSubmit = (
    event: React.FormEvent<HTMLFormElement>,
  ) => {
    event.preventDefault();

    if (!title.trim()) {
      return;
    }

    onSubmit({
      title: title.trim(),
      description: description.trim() || null,
      priority,
    });

    setTitle("");
    setDescription("");
    setPriority("medium");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4"
    >
      <div>
        <label
          htmlFor="task-title"
          className="block text-sm font-medium text-text"
        >
          Title
        </label>

        <input
          id="task-title"
          value={title}
          onChange={(event) =>
            setTitle(event.target.value)
          }
          className="mt-1 block w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text"
          placeholder="Follow up with customer"
          disabled={isSubmitting}
        />
      </div>

      <div>
        <label
          htmlFor="task-description"
          className="block text-sm font-medium text-text"
        >
          Description
        </label>

        <textarea
          id="task-description"
          value={description}
          onChange={(event) =>
            setDescription(event.target.value)
          }
          rows={3}
          className="mt-1 block w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text"
          placeholder="Add task details..."
          disabled={isSubmitting}
        />
      </div>

      <div>
        <label
          htmlFor="task-priority"
          className="block text-sm font-medium text-text"
        >
          Priority
        </label>

        <select
          id="task-priority"
          value={priority}
          onChange={(event) =>
            setPriority(
              event.target.value as TaskPriority,
            )
          }
          className="mt-1 block w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text"
          disabled={isSubmitting}
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>

      <Button
        type="submit"
        disabled={isSubmitting || !title.trim()}
      >
        {isSubmitting ? "Creating..." : "Add Task"}
      </Button>
    </form>
  );
}