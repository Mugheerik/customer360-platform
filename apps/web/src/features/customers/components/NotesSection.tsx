import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";
import { useState } from "react";

import Button from "@/components/ui/button";
import Card from "@/components/ui/card";

import { NoteService } from "../api/note.api";

type NotesSectionProps = {
  customerId: string;
};

export default function NotesSection({
  customerId,
}: NotesSectionProps) {
  const queryClient = useQueryClient();

  const [content, setContent] = useState("");

  const notesQuery = useQuery({
    queryKey: [
      "customers",
      customerId,
      "notes",
    ],
    queryFn: () =>
      NoteService.getCustomerNotes(customerId),
    enabled: Boolean(customerId),
  });

  const createNoteMutation = useMutation({
    mutationFn: () =>
      NoteService.createNote(customerId, {
        content: content.trim(),
      }),

    onSuccess: async () => {
      setContent("");

      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "notes",
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

  const deleteNoteMutation = useMutation({
    mutationFn: (noteId: string) =>
      NoteService.deleteNote(
        customerId,
        noteId,
      ),

    onSuccess: async () => {
      await queryClient.invalidateQueries({
        queryKey: [
          "customers",
          customerId,
          "notes",
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

  function handleSubmit(
    event: React.FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    const trimmedContent = content.trim();

    if (!trimmedContent) {
      return;
    }

    createNoteMutation.mutate();
  }

  return (
    <Card className="p-6">
      <div>
        <h2 className="text-lg font-semibold text-text">
          Notes
        </h2>

        <p className="mt-1 text-sm text-text-secondary">
          Add internal notes associated with this
          customer.
        </p>
      </div>

      <form
        onSubmit={handleSubmit}
        className="mt-6"
      >
        <textarea
          value={content}
          onChange={(event) =>
            setContent(event.target.value)
          }
          rows={4}
          placeholder="Write a note..."
          disabled={
            createNoteMutation.isPending
          }
          className="block w-full rounded-lg border border-border bg-background px-3 py-2 text-sm text-text outline-none focus:border-primary focus:ring-1 focus:ring-primary"
        />

        {createNoteMutation.isError && (
          <p className="mt-3 text-sm text-danger">
            Unable to create the note. Please try
            again.
          </p>
        )}

        <div className="mt-3 flex justify-end">
          <Button
            type="submit"
            disabled={
              createNoteMutation.isPending ||
              !content.trim()
            }
          >
            {createNoteMutation.isPending
              ? "Adding..."
              : "Add Note"}
          </Button>
        </div>
      </form>

      <div className="mt-8 space-y-4">
        {notesQuery.isLoading && (
          <p className="text-sm text-text-secondary">
            Loading notes...
          </p>
        )}

        {notesQuery.isError && (
          <p className="text-sm text-danger">
            Unable to load notes.
          </p>
        )}

        {!notesQuery.isLoading &&
          !notesQuery.isError &&
          notesQuery.data?.length === 0 && (
            <p className="text-sm text-text-secondary">
              No notes yet.
            </p>
          )}

        {notesQuery.data?.map((note) => (
          <div
            key={note.id}
            className="rounded-lg border border-border p-4"
          >
            <p className="whitespace-pre-wrap text-sm text-text">
              {note.content}
            </p>

            <div className="mt-3 flex items-center justify-between gap-4">
              <p className="text-xs text-text-secondary">
                {new Date(
                  note.created_at,
                ).toLocaleString()}
              </p>

              <Button
                type="button"
                variant="secondary"
                onClick={() =>
                  deleteNoteMutation.mutate(
                    note.id,
                  )
                }
                disabled={
                  deleteNoteMutation.isPending
                }
              >
                Delete
              </Button>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
}