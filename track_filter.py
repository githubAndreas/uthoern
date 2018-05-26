from logger import Logger


class TrackFilter:

    @staticmethod
    def unique_from_playlist_slices(playlist_slices):
        Logger.log_info('Start collecting unique title urls')

        unique_track_urls = set()

        for p_slice in playlist_slices:
            for playlist in p_slice.get_playlist_collection():
                for track in playlist.get_tracks():
                    url = track.get_uri()[14:]

                    if url not in unique_track_urls:
                        unique_track_urls.add(url)

            Logger.log_info('Slice[' + p_slice.get_info().get_item_range() + '] track urls successfully collected')

        Logger.log_info('Totally ' + str(len(unique_track_urls)) + ' unique track urls founded')

        return list(unique_track_urls)
