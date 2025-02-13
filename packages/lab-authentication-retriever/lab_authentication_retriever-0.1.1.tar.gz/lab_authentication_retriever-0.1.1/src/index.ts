import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './handler';

/**
 * Initialization data for the lab-authentication-retriever extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'lab-authentication-retriever:plugin',
  description:
    'A JupyterLab extension. that interacts with qbraid core and gets authentication details for other front end extension.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log(
      'JupyterLab extension lab-authentication-retriever is activated!'
    );

    requestAPI<any>('get-example')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The lab_authentication_retriever server extension appears to be missing.\n${reason}`
        );
      });

    requestAPI<any>('qbraid-config')
      .then(data => {
        console.log('[!] Server extension response for config', data);
      })
      .catch(reason => {
        console.error(
          `The lab_authentication_retriever server extension appears to be missing.\n${reason}`
        );
      });

    requestAPI<any>('qbraid-disc-usage')
      .then(data => {
        console.log('[!] Server extension response for disc usage', data);
      })
      .catch(reason => {
        console.error(
          `The lab_authentication_retriever server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default plugin;
